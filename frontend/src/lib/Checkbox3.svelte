<script>
  import { onMount } from 'svelte';

  export let selected = [];
  export let disabled = false;

  export let options = [];

  $: selected = options.flatMap(opt => [
    ...(opt.checked ? [opt.label] : []),
    ...(opt.children ? opt.children.filter(c => c.checked).map(c => c.label) : [])
  ]);

  async function fetchTagChoices() {
      const res = await fetch(`https://trenph.up.railway.app/api/station/?format=json`);
      if (!res.ok) throw new Error("Failed to fetch stations");

      const data = await res.json();
      data.sort((a, b) => a.id - b.id);

      const stations = ['LRT1', 'LRT2', 'MRT3'];
      let fetchedOptions = [];

      stations.forEach(line => {
        let c = data
          .filter(d => d.trainLine === line)
          .map(station => ({
            id: String(station.id),
            label: station.stationName,
            checked: selected.includes(station.stationName)
          }));
        
        fetchedOptions.push({
          id: line,
          label: line,
          checked: selected.includes(line),
          children: c
        });
      });

      options = [...fetchedOptions];
    }

  let open = false;
  function toggleDropdown() {
    open = !open;
  }

  let dropdownRef;
  function handleClickOutside(event) {
    if (dropdownRef && !dropdownRef.contains(event.target)) {
      open = false;
      openParent = null;
    }
  }

  onMount(() => {
    document.addEventListener('click', handleClickOutside);
    fetchTagChoices();
  });
  let openParent = null;

  function toggleChildren(parentId) {
    event.stopPropagation();
    openParent = openParent === parentId ? null : parentId;
  }
</script>

<div class="relative inline-block text-left" bind:this={dropdownRef}>
  <button
    on:click={toggleDropdown}
    class="text-black {options.length && !disabled ? "hover:bg-gray-200" : ""} text-sm inter-body rounded-lg px-4 py-2 inline-flex items-center border-1 border-neutral-300"
    type="button"
    disabled={disabled || !options.length}
  >
    Filter

    {#if selected.length}
      <span class="text-white ml-1.5 text-[10px] bg-blue-600 rounded-full w-5 h-5 flex items-center justify-center">
        {selected.length}
      </span>
    {/if}

    <svg class="w-2.5 h-2.5 ms-3 {open ? "rotate-180" : ""}" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
    </svg>
  </button>

  {#if open}
      <div class="absolute mt-2 z-10 w-56 bg-white divide-y divide-gray-100 rounded-lg shadow-sm max-h-60 overflow-y-auto">
      <ul class="p-3 space-y-3 text-sm text-gray-700">
        {#each options as option}
          <li class="group">
            <div class="flex items-center justify-between hover:bg-gray-100 rounded p-1">
              <button class="flex items-center" on:click={() => option.checked = !option.checked}>
                <input
                  id={option.id}
                  type="checkbox"
                  bind:checked={option.checked}
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500"
                />
                <label for={option.id} class="ms-2 text-sm inter-body font-medium text-gray-900">
                  {option.label}
                </label>
              </button>
              {#if option.children}
                <button
                  on:click={() => toggleChildren(option.id)}
                  class="ml-2 p-1 rounded hover:bg-gray-200 focus:outline-none focus:ring focus:ring-blue-300"
                  aria-label="Toggle submenu"
                >
                  {#if openParent == option.id}
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      class="w-4 h-4 text-gray-600 rotate-180"
                    >
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                  {:else}
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      class="w-4 h-4 text-gray-600"
                    >
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                  {/if}
                </button>
            
              {/if}
            </div>

            {#if option.children && openParent === option.id}
              <ul class="pl-6 mt-2 space-y-2">
                {#each option.children as child}
                  <li>
                    <div class="flex items-center hover:bg-gray-100 rounded p-1">
                      <input
                        id={child.id}
                        type="checkbox"
                        bind:checked={child.checked}
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500"
                      />
                      <label for={child.id} class="ms-2 text-sm inter-body font-medium text-gray-900">
                        {child.label}
                      </label>
                    </div>
                  </li>
                {/each}
              </ul>
            {/if}
          </li>
        {/each}
      </ul>
    </div>
  {/if}
</div>

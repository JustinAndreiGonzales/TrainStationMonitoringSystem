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
    {#if selected.length}
      <span class="text-white ml-[-5px] mr-1.5 text-[10px] bg-blue-600 rounded-full w-5 h-5 flex items-center justify-center">
        {selected.length}
      </span>
    <!--
    {:else}
      <svg class="w-5 h-5 mr-2" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd" viewBox="0 0 487 511.954"><path fill-rule="nonzero" d="M0 52.894h146.098a70.42 70.42 0 0118.388-32.26C177.18 7.874 194.783 0 214.13 0c19.37 0 36.95 7.874 49.645 20.569s20.569 30.275 20.569 49.644c0 19.348-7.874 36.95-20.569 49.645-12.76 12.673-30.319 20.569-49.645 20.569-19.282 0-36.884-7.896-49.579-20.569-8.79-8.812-15.29-19.936-18.453-32.326H0V52.894zm392.096 201.698a35.528 35.528 0 00-10.404-25.172 35.526 35.526 0 00-25.172-10.404 35.562 35.562 0 00-25.171 10.404c-6.413 6.369-10.404 15.334-10.404 25.172 0 9.837 3.991 18.802 10.382 25.193 6.391 6.391 15.356 10.382 25.193 10.382 9.837 0 18.802-3.991 25.193-10.382a35.728 35.728 0 0010.383-25.193zm14.069-49.645a70.26 70.26 0 0118.409 32.326h62.405v34.637h-62.405a70.366 70.366 0 01-18.409 32.326c-12.761 12.673-30.319 20.569-49.645 20.569-19.282 0-36.884-7.896-49.579-20.569-12.738-12.76-20.634-30.362-20.634-49.644 0-19.326 7.896-36.885 20.569-49.58 12.694-12.76 30.297-20.634 49.644-20.634 19.369 0 36.95 7.874 49.645 20.569zM260.11 271.91H0v-34.637h260.11v34.637zM67.007 424.421a70.414 70.414 0 0118.388-32.26c12.694-12.76 30.297-20.634 49.644-20.634 19.369 0 36.95 7.874 49.645 20.569 12.694 12.694 20.569 30.275 20.569 49.644 0 19.347-7.875 36.95-20.569 49.645-12.76 12.672-30.319 20.569-49.645 20.569-19.282 0-36.884-7.897-49.579-20.569-8.79-8.813-15.29-19.937-18.453-32.326H0v-34.638h67.007zm42.839-7.852c-6.391 6.369-10.382 15.334-10.382 25.171s3.991 18.802 10.382 25.193c6.391 6.391 15.356 10.383 25.193 10.383 9.838 0 18.803-3.992 25.193-10.383a35.728 35.728 0 0010.383-25.193 35.525 35.525 0 00-35.576-35.576 35.654 35.654 0 00-25.193 10.405zm121.603 7.852h255.508v34.638H231.449v-34.638zM188.937 45.042c-6.391 6.369-10.382 15.334-10.382 25.171 0 9.838 3.991 18.802 10.382 25.193 6.391 6.391 15.356 10.383 25.193 10.383 9.838 0 18.802-3.992 25.193-10.383a35.725 35.725 0 0010.383-25.193 35.524 35.524 0 00-35.576-35.575 35.653 35.653 0 00-25.193 10.404zm121.603 7.852H487v34.638H310.54V52.894z"/></svg>
    -->
    {/if}
    
    Filter

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

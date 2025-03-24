<script>
  export let selected = [];
  export let disabled = false;

  export let options = [
    { id: 'checkbox-item-1', label: 'LRT-1', checked: false },
    { id: 'checkbox-item-2', label: 'LRT-2', checked: false },
    { id: 'checkbox-item-3', label: 'MRT-3', checked: false }
  ];

  $: selected = options.filter(opt => opt.checked).map(opt => opt.label);

  let open = false;
  function toggleDropdown() {
    open = !open;
  }

</script>

<div class="relative inline-block text-left">
  <button
    on:click={toggleDropdown}
    class="text-neutral-500 outline-gray-500 hover:bg-gray-200 text-sm inter-body rounded-bl-lg px-4 py-2 inline-flex items-center border-r border-gray-300"
    type="button"
    disabled={disabled}
  >
    Tags
    <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
    </svg>
  </button>

  {#if open}
    <div class="absolute mt-2 z-10 w-48 bg-white divide-y divide-gray-100 rounded-lg shadow-sm">
      <ul class="p-3 space-y-3 text-sm text-gray-700">
        {#each options as option}
          <li>
            <div class="flex items-center">
              <input
                id={option.id}
                type="checkbox"
                bind:checked={option.checked}
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500"
              />
              <label for={option.id} class="ms-2 text-sm inter-body font-medium text-gray-900">
                {option.label}
              </label>
            </div>
          </li>
        {/each}
      </ul>
    </div>
  {/if}
</div>

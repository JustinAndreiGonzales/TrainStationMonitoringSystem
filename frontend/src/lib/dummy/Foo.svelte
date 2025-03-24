<script>
  export let text;
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch('openBar', { text });
  }
</script>

<div class="flex items-center space-x-2">
  <p>{text}</p>
  <button on:click={handleClick} class="px-2 py-1 bg-blue-500 text-white rounded">Open Bar</button>
</div>

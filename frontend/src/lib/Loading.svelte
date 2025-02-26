<script lang="ts">
  import { onMount, onDestroy } from 'svelte';

  export let message = 'Loading';
  let dots = '';
  let interval;

  onMount(() => {
      interval = setInterval(() => {
          dots = ".".repeat((dots.length % 3) + 1);
      }, 300);
  });

  onDestroy(() => {
      clearInterval(interval);
  });
</script>

<p class="text-gray-500 text-lg text-center inter-body">{message}{dots}</p>

<script>
    export let data;
</script>

<!-- REMOVE/REPLACE -->
{#if data.error}
  <p class="text-red-500">{data.error}</p>
{:else}
  <h1 class="text-2xl font-bold">Protected Data</h1>
  <pre class="bg-gray-100 p-4 rounded">{JSON.stringify(data.data, null, 2)}</pre>
{/if}
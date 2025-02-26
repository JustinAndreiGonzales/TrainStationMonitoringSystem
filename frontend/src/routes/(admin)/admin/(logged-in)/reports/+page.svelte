<script>
  import ReportsList from '$lib/ReportsList.svelte'
    export let data;
</script>


<title>Reports | Train Station Monitoring System</title>

<div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
  <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Reports</h1>

  {#if data.error}
    <p class="text-red-500">{data.error}</p>
  {:else}
    <ReportsList posts={data.data} /> 
  {/if}
</div>
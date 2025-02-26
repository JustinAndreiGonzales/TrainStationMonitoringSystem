<script>
  import ReportsList from '$lib/ReportsList.svelte'
  import Popup from '$lib/Popup.svelte'
  import Loading from '$lib/Loading.svelte'

  export let data;
</script>


<title>Reports | Train Station Monitoring System</title>

{#await data}
<div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
  <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Reports</h1>
  <Loading />
</div>
{:then result}
  {#if result.error}
    <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
      <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Reports</h1>
    </div>
      <Popup message={"Error: " + result.error} href={"/admin/home"} text={"✕"} />
  {:else}
    <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
      <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Reports</h1>
      <ReportsList posts={result.data} />
    </div>
  {/if}
{/await}
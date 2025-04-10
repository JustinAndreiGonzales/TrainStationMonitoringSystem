<script>
  import ReportsList from '$lib/ReportsList.svelte'
  import Popup from '$lib/Popup.svelte'
  import Loading from '$lib/Loading.svelte'
  import Checkbox from '$lib/Checkbox3.svelte';
  import GoToButton from '$lib/GoToButton.svelte';
  import { onMount } from 'svelte';

  let allData = [];
  let url = 'https://trenph.up.railway.app/api/reports/?format=json';
  let boo = false;
  let current = 5;
  let filters = [];
  let result = '';

  let openToDel = false;
  let readyToDel = false;

  function toggleLoad() {
    boo = !boo;
    current += 5;
  }

  async function refreshAccessToken() {
    const refreshToken = localStorage.getItem('refresh_token');
    if (!refreshToken) {
      throw new Error('No refresh token available.');
    }

    let res;
    try {
      res = await fetch('https://trenph.up.railway.app/api/token/refresh/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ refresh: refreshToken })
      });      
    } catch {
      throw new Error('Error refreshing token.');
    }

    const data = await res.json();
    localStorage.setItem('jwt_token', data.access);
    localStorage.setItem('refresh_token', data.refresh);

    return data.access;
  }  

  async function fetchReports(token = localStorage.getItem('jwt_token')) {
    let res;

    if(!url) {
      return;
    }
    if (url.startsWith("http://")) {
      url = "https://" + url.substring(7);
    }

    try {
      res = await fetch(url, {
        method: 'GET',
        headers: { 'Authorization': `Bearer ${token}` },
      });
    } catch (error) {
      throw new Error(error);
    }

    const data = await res.json();
    url = data.next;

    allData = [...allData, ...data.results];
  }

  async function fetchMoreReports() {
    const token = await refreshAccessToken();
    await fetchReports(token);
    toggleLoad();
  }

  $: allData = allData;

  //**
  onMount(() => {
    allData = [];
    url = 'https://trenph.up.railway.app/api/reports/?format=json';
  });
  //
</script>

<title>Reports | Train Station Monitoring System</title>

{#await fetchReports()}
  <div class="flex-col items-center scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7 mx-20">  
    <div class="flex flex-col items-center justify-center inter-h1 text-3xl origin-top mt-6 space-y-2">
      <h1>Reports</h1>
      <Checkbox disabled={true}/>
    </div>
    <Loading />
  </div>
{:catch e}
  <div class="flex-col items-center scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7 mx-20">  
    <div class="flex flex-col items-center justify-center inter-h1 text-3xl origin-top mt-6 space-y-2">
      <h1>Reports</h1>
      <Checkbox disabled={true}/>
    </div>
  </div>
  <Popup message={"Error! No database connection"} href={"/admin/home"} text={"✕"} />
{:then token}
  {#if !boo}
  <div class="flex-col items-center scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7 mx-20">  
    <div class="flex flex-col items-center justify-center inter-h1 text-3xl origin-top mt-6 space-y-2">
      <h1>Reports</h1>
      <Checkbox bind:selected={filters} />
    </div>
    <div class="flex flex-col items-center justify-center">
      <ReportsList posts={allData} filters={filters} bind:result={result} bind:openToDel={openToDel} bind:readyToDel={readyToDel}/>
        {#if url != null}
        <button
          class="max-w-sm bg-gray-200 hover:bg-gray-300 py-2 px-4 rounded inter-body text-[13px] -mt-17 mb-24"
          on:click={toggleLoad}
        >
          Load more ↓
        </button>
        {/if}
    </div>
  </div>
  {:else}
    {#await fetchMoreReports()}
    <div class="flex-col items-center scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7 mx-20">  
      <div class="flex flex-col items-center justify-center inter-h1 text-3xl origin-top mt-6 space-y-2">
        <h1>Reports</h1>
        <Checkbox bind:selected={filters}/>
      </div>

      <ReportsList posts={allData} filters={filters} bind:result={result} bind:openToDel={openToDel} bind:readyToDel={readyToDel}/>
      <div class="-mt-25 mb-24">
        <Loading />
      </div>
    </div>
    {:catch error}
      <Popup message={"Error! No database connection"} href={"/admin/home"} text={"✕"} />
    {:then tokens}
      {toggleLoad()}
      <br>
    {/await}
  {/if}
{/await}

{#if result}
<div class="fixed inset-0 z-50 flex items-center justify-center">
  {#if result.includes("Error!")}
      <Popup message={result} href={"/admin/home"} text={"✕"} />
    {:else}
      <Popup message={result} href={"/admin/reports"} text={"✕"} color="bg-green-700" txtColor="text-green-700" />
    {/if}
</div>
{/if}

{#if !result && openToDel}
  <div class="fixed inset-0 backdrop-blur-[2px] z-40"></div>
    <div
      class={`fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-4/5 sm:w-auto bg-gray-300 text-black text-lg rounded-lg shadow-lg p-8 z-50`}
      role="alert"
    >
      <div class="flex flex-col items-center justify-center justify-between m-auto space-y-2.5">
        <span class="flex text-left inter-body font-xs">Are you sure you want to delete this report?</span>
        <span class="flex space-x-4 inter-body text-sm">
          <button class="py-1.5 px-2 text-white rounded-lg bg-red-500 hover:bg-red-700" on:click={() => readyToDel = true}>Delete</button>
          <button class="py-1.5 px-2 text-black rounded-lg bg-white hover:bg-gray-200" on:click={() => openToDel = false}>Cancel</button>
        </span>
      </div>
    </div>
{/if}
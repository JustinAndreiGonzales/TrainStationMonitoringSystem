<script lang="ts">
  import Popup from '$lib/Popup.svelte';
  import Loading from "$lib/Loading.svelte"
  
  import { onMount } from 'svelte';

  let id = '';

  let subject = '';
  let body = '';
  let stationName = '';

  let loading = true;
  let error = '';
  
  onMount(() => {
      const url = new URL(window.location.href);
      const queryParams = new URLSearchParams(url.search);
      id = queryParams.get('id') || '';
      loading = false;
  });

  const getStationInfo = async (id: string) => {
    const res = await fetch('https://trenph.up.railway.app/api/station/?format=json');
      if (!res.ok) throw new Error("Error! No database connection");
      const data = await res.json();

      const ret = data.find(station => (station.id).toString() === id);

      stationName = ' - ' + ret.stationName + ' ('+  ret.trainLine +  ')';
      return ret;
  }
  
  async function postReport(station, line) {
    if (subject && body) {
      const res = await fetch('https://trenph.up.railway.app/api/reports/create/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          subject: subject,
          station: line + ',' + station,
          body: body,
        })  
      })

      if (!res.ok) {
        error = 'Error! No database connection'
      }
      else {
        error = 'done';
      }
    }
    else if (!subject && !body){
      error = 'both'
    }
    else if (!subject){
      error = 'title'
    }
    else {
      error = 'details'
    }
  }
</script>

<title>Report Issue | Train Station Monitoring System</title>

<h1 class="text-center inter-h1 text-2xl sm:text-3xl origin-top mt-6">Report Issue{stationName}</h1>
<br>
{#if !loading}
  {#if id}
    {#await getStationInfo(id)}
      <Loading />
    {:then station}
      <div class="scale-80 sm:scale-100 md:scale-100 origin-top flex flex-col justify-center items-center space-y-3">
        <div class="flex flex-col justify-center items-center space-y-3 w-96">
          <input type="text" id="title" bind:value={subject} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-2.5 inter-body" placeholder="Title" required />
          <textarea rows="50" id="details" bind:value={body} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full h-50 p-2.5 dark:bg-gray-700 inter-body resize-none" placeholder="Write details here..." required></textarea>
          <button
            class="max-w-sm mx-auto bg-blue-600 hover:bg-blue-700 text-white inter-body text-sm w-full py-2 px-4 rounded"
            on:click={postReport(station.stationName, station.trainLine)}
          >
            Submit
          </button> 
        </div>
        
        {#if error == 'both' }
          <p class='inter-body text-sm text-red-500'>Report is incomplete and missing {error} fields.</p>
        {/if}
        {#if error == 'title' || error == 'details' }
          <p class='inter-body text-sm text-red-500'>Report is incomplete and missing {error}.</p>
        {/if}
      </div>

      {#if error }
        {#if error == 'done'}
          <Popup message={"Report has been submitted successsfully!"} color='bg-green-700' txtColor='text-green-600' href={`/`} text={"✕"} />
        {:else if error != 'title' && error != 'details' && error != 'both'}
          <Popup message={error} href={`/`} text={"✕"} />
        {:else}
          <br>    
        {/if}
      {/if}
    
    {:catch err}
      <Popup message={err} href={"/"} text={"✕"} />
    {/await}
  {:else}
    <Popup message={"Please select station first"} href={"/stations"} text={"✕"} />
  {/if}
{/if}


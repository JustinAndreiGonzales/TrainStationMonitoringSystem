<script lang="ts">
  import Popup from '$lib/Popup.svelte';
  import Loading from "$lib/Loading.svelte"
  
  import { onMount } from 'svelte';

  let id = '';
  let subject = '';
  let body = '';
  
  onMount(() => {
      const url = new URL(window.location.href);
      const queryParams = new URLSearchParams(url.search);
      id = queryParams.get('id') || '';
  });

  const getStationInfo = async (id: string) => {
    const res = await fetch('https://trenph.up.railway.app/api/station/?format=json');
      if (!res.ok) throw new Error("Failed to fetch stations");
      const data = await res.json();

      return data.find(station => (station.id).toString() === id);
  }
</script>


<!-- BIND: @ station.stationName -->
<title>Report Issue | Train Station Monitoring System</title>

<h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Report</h1>
<br>

{#if id}
  {#await getStationInfo(id)}
    <Loading />
  {:then station}
    <div class="scale-80 sm:scale-100 md:scale-100 origin-top flex flex-col justify-center items-center space-y-3">
      <div class="flex flex-col justify-center items-center space-y-3 w-96">
        <!-- REMOVE: when done -->
        <p>{station.stationName}</p>
        <input type="text" id="title" bind:value={subject} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-2.5 inter-body" placeholder="Title" required />
        <textarea rows="50" id="details" bind:value={body} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full h-50 p-2.5 dark:bg-gray-700 inter-body resize-none" placeholder="Write details here..." required></textarea>
        <button
          class="max-w-sm mx-auto bg-blue-600 hover:bg-blue-700 text-white inter-body text-sm w-full py-2 px-4 rounded"
        >
          Submit
        </button>
        <!-- ADD: no db connection? -->
      </div>
    </div>
  {/await}
  <!-- ADD: no db connection -->
{:else}
  <!-- FIX: popup appears for split second -->
  <Popup message={"Please select station first"} href={"/stations"} text={"✕"} />
{/if}


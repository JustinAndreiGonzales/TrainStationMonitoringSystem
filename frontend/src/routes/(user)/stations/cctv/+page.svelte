<script lang="ts">
  import Popup from '$lib/Popup.svelte';
  import Loading from "$lib/Loading.svelte"
  
  import { onMount } from 'svelte';

  let id = '';
  let station = '';

  let loading = true;  
  let selectedStream = '';

  
  onMount(() => {
      const url = new URL(window.location.href);
      const queryParams = new URLSearchParams(url.search);
      id = queryParams.get('id') || '';
      loading = false;
  });

  const getStationInfo = async (id: string) => {
    // FIX: replace w url
    const res = await fetch('https://trenph.up.railway.app/api/station/?format=json');
      if (!res.ok) throw new Error("Failed to fetch stations");
      const data = await res.json();

      // REMOVE: find
      const ret = data.find(station => (station.id).toString() === id);

      station = ret.stationName + ' ('+  ret.trainLine +  ') - ';
      return ret;
  }

  // include fetch from station
</script>


<title>View CCTV | Train Station Monitoring System</title>

<h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">{station}CCTV Feed</h1>
<br>

{#if loading}
  <br>
{:else}
  {#if id}
    {#await getStationInfo(id)}
      <Loading />
    {:then station}
      <div class="scale-80 sm:scale-100 md:scale-100 origin-top flex flex-col justify-center items-center space-y-3">
        <div class="flex flex-col justify-center items-center space-y-5 w-lg">
          <select
            id="stations"
            class="inter-body bg-gray-50 border border-gray-300 text-gray-900 text-[13px] rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            bind:value={selectedStream}
          >
            <!-- FIX: cctv loop for fetch -->
            <option value="" selected>Select CCTV stream</option>
            {#each station}
              <!--
              {#each station}
              <option value={cctv stream link}>CCTV{left or right}</option>
              -->
              <option value="/stations?id={id}">{station.stationName}</option>
            {/each}
            <option value="https://www.youtube.com/embed/dQw4w9WgXcQ">Rick Roll</option>
            <option value="https://res.cloudinary.com/stations-cctv/video/upload/station-1_cctv.mp4">Blank Space</option>
          </select>
          
          <!-- FIX: autoplay + default with no selection? -->
          <iframe title="cctv" class="w-full aspect-video ... rounded-lg" src={selectedStream}></iframe>
        </div>
      </div>
    {:catch err}
      <Popup message={err} href={"/"} text={"✕"} />
    {/await}
  {:else}
    <Popup message={"Please select station first"} href={"/stations"} text={"✕"} />
  {/if}
{/if}


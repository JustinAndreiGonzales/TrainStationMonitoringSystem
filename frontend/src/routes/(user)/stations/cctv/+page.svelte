<script lang="ts">
  import Popup from '$lib/Popup.svelte';
  import Loading from "$lib/Loading.svelte";
  
  import { onMount } from 'svelte';

  let id = '';
  let stream = '';
  let loading = true;  

  let selectedStation = '';
  let selectedStream = '';

  
  onMount(() => {
      const url = new URL(window.location.href);
      const queryParams = new URLSearchParams(url.search);
      id = queryParams.get('id') || '';
      stream = queryParams.get('stream') || '';
      loading = false;
  });

  const getStationInfo = async (id: string) => {
    const res = await fetch(`https://trenph.up.railway.app/api/station/${id}/?format=json`);
      if (!res.ok) throw new Error("Failed to fetch stations");
      const data = await res.json();

      selectedStation = ' - ' + data.stationName + ' ('+  data.trainLine +  ')';

      console.log("hi" + selectedStream);
      return data;
  }

  
</script>


<title>View CCTV | Train Station Monitoring System</title>

{#if loading}
  <br>
{:else}
  {#if id}
    {#await getStationInfo(id)}
      <div class="flex justify-center items-center min-h-screen">
        <Loading />
      </div>
    {:then station}
      <div class="scale-80 sm:scale-100 md:scale-100 origin-top flex flex-col justify-center items-center space-y-3">
        <h1 class="flex justify-center text-center inter-h1 text-3xl origin-top mt-6">CCTV Feed {stream}{selectedStation}</h1>
        <br>
        <!-- <div class="flex flex-col justify-center items-center space-y-5 w-lg"> -->
        {#if stream == "1"}
          <video 
            class="w-full aspect-video rounded-lg object-cover" 
            src={station.leftCCTV} autoplay loop muted playsinline
          ></video>
        {:else}
          <video 
            class="w-full aspect-video rounded-lg object-cover" 
            src={station.rightCCTV} autoplay loop muted playsinline
          ></video>
        {/if}
      </div>
      <!--
      {#if station.leftCCTV || station.rightCCTV}
      <div class="scale-70 sm:scale-100 md:scale-100 origin-top flex flex-col justify-center items-center space-y-3">
        <div class="flex flex-col justify-center items-center space-y-5 w-lg">
          
          <form class="w-full flex flex-col space-y-2">
            <select
              id="stations"
              class="inter-body bg-gray-50 border border-gray-300 text-gray-900 text-[13px] rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              on:change={(e) => selectedStream = e.target.value}
            >
              <option value='' selected>Select CCTV stream</option>
              {#if station.leftCCTV}
                <option value={station.leftCCTV}>CCTV 1</option>
              {/if}
              {#if station.rightCCTV}
                <option value={station.rightCCTV}>CCTV 2</option>
              {/if}
            </select>
          </form>
          
          {#if selectedStream}
            <video 
              class="w-full aspect-video rounded-lg object-cover" 
              src={selectedStream} autoplay loop muted playsinline
            ></video>
          {:else}
            <img alt="cctv" class="w-full aspect-video object-cover rounded-lg" src="/empty_cctv.png" />
          {/if}
        </div>
      </div>
      {:else}
        <div class="scale-80 sm:scale-100 md:scale-100 origin-top flex flex-col justify-center items-center space-y-3">
          <div class="flex flex-col justify-center items-center space-y-5 w-lg">
            <form class="w-full flex flex-col space-y-2">
              <select
                id="stations"
                class="inter-body bg-gray-50 border border-gray-300 text-gray-900 text-[13px] rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              >
                <option value='' selected>Select CCTV stream</option>
            </form>
            
            <img alt="cctv" class="w-full aspect-video object-cover rounded-lg" src="/empty_cctv.png" />
          </div>
        </div>
        <Popup message={'Error! No currently available CCTVs'} href={`/stations?id=${id}`} text={"✕"} />
      {/if}
      -->
    {:catch err}
      <div class="flex justify-center items-center min-h-screen">
        <Popup message={err} href={"/"} text={"✕"} />
      </div>
    {/await}
  {:else}
    <div class="flex justify-center items-center min-h-screen">
      <Popup message={"Please select station first"} href={"/stations"} text={"✕"} />
    </div>
  {/if}
{/if}


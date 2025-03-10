<script lang="ts">
  import DropdownStations from '$lib/DropdownStations.svelte';
  import DropdownStations2 from '$lib/DropdownStations2.svelte';
  import Popup from '$lib/Popup.svelte';
  import Loading from '$lib/Loading.svelte';
  import trainMap from '$lib/images/train_map.png';
  import { onMount } from 'svelte';

  let start = '';

  onMount(() => {
      const url = new URL(window.location.href);
      const queryParams = new URLSearchParams(url.search);
      start = queryParams.get('start') || '';
  });

  async function fetchStations() {
      const res = await fetch('https://trenph.up.railway.app/api/station/?format=json');
      if (!res.ok) throw new Error("Failed to fetch stations");
      return await res.json();
  }

  const getStationInfo = async (start: string) => {
    const res = await fetch(`https://trenph.up.railway.app/api/station/${start}/?format=json`)
    const data = await res.json();
    console.log(start)
    return data;
  }
</script>

<title>Routes | Train Station Monitoring System</title>

<div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6">
  {#if start}
    {#await getStationInfo(start)}
      <Loading />
    {:then station}
      {#if station.isOperating}
        <p class="flex justify-center inter-h1 text-3xl">Station: {station.stationName}</p>
        <p class="flex justify-center inter-body text-3xl">ETA = {station.leftETA} vs {station.rightETA}</p>
        <p class="flex justify-center inter-body text-3xl">Density = {station.leftCurrentDensity} vs {station.rightCurrentDensity}</p>
      {:else}
        <h1 class="flex justify-center inter-h1 text-3xl">Stations</h1>
      
        <br>
      
        <div class="flex justify-center items-center">
          <img src={trainMap} alt="Train Map" class="max-w-full w-[385px] h-auto rounded-lg">
        </div>

        <br>

        <DropdownStations allStations={[]}/>
        <Popup message={`Error: ${station.stationName} station is currently not operational!`} href={"/stations"} text={"✕"} />

      {/if}
    {:catch err}
      <h1 class="flex justify-center inter-h1 text-3xl">Routes</h1>
      <!-- PARSE INPUT-->
          
    {/await}
    
  {:else}
    <h1 class="flex justify-center inter-h1 text-3xl">Routes</h1>

    <br>

    <div class="flex justify-center items-center">
        <img src={trainMap} alt="Train Map" class="max-w-full w-[385px] h-auto rounded-lg">
    </div>

    <br>

    {#await fetchStations()}
      <Loading />
    {:then stations}
      <!-- FIX: combine to single component? -->
      <DropdownStations2 allStations={stations}/>
    {:catch error}
      <Popup message={error} href={"/"} text={"✕"} />
    {/await}

  {/if}
</div>


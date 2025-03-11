<script lang="ts">
  import DropdownStations from '$lib/DropdownStations.svelte';
  import Popup from '$lib/Popup.svelte';
  import trainMap from '$lib/images/train_map.png';
  import GoToButton from '$src/lib/GoToButton.svelte';
  import Loading from '$lib/Loading.svelte'
  import { onMount } from 'svelte';

  let id = '';
  let loading = true;

  onMount(() => {
      const url = new URL(window.location.href);
      const queryParams = new URLSearchParams(url.search);
      id = queryParams.get('id') || '';
      loading = false;
  });

  async function fetchStations() {
    const res = await fetch('https://trenph.up.railway.app/api/station/?format=json');
    if (!res.ok) throw new Error("Failed to fetch stations");
    return await res.json();
  }

  const getStationInfo = async (id: string) => {
    const res = await fetch(`https://trenph.up.railway.app/api/station/${id}/?format=json`)
    const data = await res.json();
    console.log(id)
    return data;
  }
</script>

<title>Stations | Train Station Monitoring System</title>

{#if !loading}
  {#if id}
    {#await getStationInfo(id)}
      <!-- FIX MAYBE: show page -->
      <div class="flex justify-center items-center min-h-screen">
        <Loading />
      </div>
    {:then station}
      {#if station.isOperating}
        <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6">
          <div class="flex flex-col justify-center items-center space-y-1">
            <div class="flex flex-row items-end bg-gray-200 p-5 rounded-lg space-x-10">
              <div>
                <p class="inter-h1 text-2xl">{station.stationName}</p>
                <p class="inter-body text-2xl">{station.trainLine}</p>
              </div>

              <GoToButton text="report" href={`/stations/report?id=${station.id}`}/>
            </div>

            <p class="inter-body text-3xl">ETA = {station.leftETA} vs {station.rightETA}</p>
            <p class="inter-body text-3xl">Density = {station.leftCurrentDensity} vs {station.rightCurrentDensity}</p>
          
            <GoToButton text="cctv" href={`/stations/cctv?id=${station.id}`}/>
          </div>
        </div>
      {:else}
        <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6">
          <h1 class="flex justify-center inter-h1 text-3xl">Stations</h1>
        
          <br>
          <div class="flex justify-center items-center">
            <img src={trainMap} alt="Train Map" class="max-w-full w-[385px] h-auto rounded-lg">
          </div>

          <br>
          <DropdownStations allStations={[]}/>
        </div>

        <Popup message={`Error: ${station.stationName} station is currently not operational!`} href={"/stations"} text={"✕"} />  
        {/if}
    {/await}
  
  {:else}
    {#await fetchStations()}
      <!-- FIX MAYBE: show page -->
      <div class="flex justify-center items-center min-h-screen">
        <Loading />
      </div>
    {:then stations}
      <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6">
        <h1 class="flex justify-center inter-h1 text-3xl">Stations</h1>
    
        <br>
    
        <div class="flex justify-center items-center">
            <img src={trainMap} alt="Train Map" class="max-w-full w-[385px] h-auto rounded-lg">
        </div>
    
        <br>
        <DropdownStations allStations={stations}/>
      </div>
    {:catch error}
      <!-- FIX: show page -->
      <Popup message={error} href={"/"} text={"✕"} />
    {/await}
  
  {/if}
{/if}

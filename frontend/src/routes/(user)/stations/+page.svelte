<script lang="ts">
  import DropdownStations from '$lib/DropdownStations.svelte';
  import Popup from '$lib/Popup.svelte';
  import trainMap from '$lib/images/train_map.png';
  import GoToButton from '$src/lib/GoToButton.svelte';
  import Loading from '$lib/Loading.svelte';
  import RadioButton from '$lib/RadioButton.svelte';
  import { onMount } from 'svelte';

  let id = '';
  let loading = true;
  let selected = 0;

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
    // ERROR!
    const data = await res.json();
    console.log(id)
    return data;
  }

  const getHourlyDensity = async (id: string) => {
    let data1 = [];
    let data2 = [];

    const res1 = await fetch(`https://trenph.up.railway.app/api/station/${id}/hourly-density/left?format=json`)
    const res2 = await fetch(`https://trenph.up.railway.app/api/station/${id}/hourly-density/right?format=json`)
    if (!res1.ok && !res2.ok) throw new Error("Failed to fetch stations");

    if (res1.ok){
      data1 = await res1.json();
    }
    
    if (res2.ok) {
      data2 = await res2.json();
    }
    
    return [data1, data2];
  }

  const getDailyDensity = async (id: string) => {
    let data1 = [];
    let data2 = [];

    const res1 = await fetch(`https://trenph.up.railway.app/api/station/${id}/daily-density/left?format=json`)
    const res2 = await fetch(`https://trenph.up.railway.app/api/station/${id}/daily-density/right?format=json`)
    if (!res1.ok && !res2.ok) throw new Error("Failed to fetch stations");
    
    if (res1.ok){
      data1 = await res1.json();
    }

    if (res2.ok) {
      data2 = await res2.json();
    }
    
    return [data1, data2];
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
            <!-- DIV1 - HEADER -->
            <div class="flex flex-row items-end bg-gray-200 p-5 rounded-lg space-x-10">
              <div>
                <p class="inter-h1 text-2xl">{station.stationName}</p>
                <p class="inter-body text-2xl">{station.trainLine}</p>
              </div>

              <GoToButton text="report" href={`/stations/report?id=${station.id}`}/>
            </div>

            <!-- DIV2 - ETA -->
            <div class="flex flex-col items-center justify-center bg-gray-200 p-5 rounded-lg space-x-10">
              <p class="inter-body text-3xl">ETA = {station.leftETA} vs {station.rightETA}</p>
            </div>

            <!-- DIV3 - CURRENT DENSITY -->
            <div class="flex flex-col items-center justify-center bg-gray-200 p-5 rounded-lg space-x-10">
              <p class="inter-body text-3xl">Current density {station.leftCurrentDensity} vs {station.rightCurrentDensity}</p>
              <GoToButton text="View cctv" href={`/stations/cctv?id=${station.id}`}/>
            </div>

            <!-- DIV4 - DAILY DENSITY -->

            <!-- DIV5 - HOURLY DENSITY -->
            <!-- DUPLICATE: for hourly density -->
            <div class="flex flex-col items-center justify-center bg-gray-200 rounded-lg space-x-10">
              <p class="inter-h1">Daily density</p>

              <RadioButton options={["Left", "Right"]} values={[0, 1]} bind:selected={selected} />

              {#await getDailyDensity(id)}
                <Loading />
              {:then daily}
                <!-- FIX: BUTTON details -->
                <!-- ADD: graph of density -->
                <p class="inter-body">{daily[selected].length} {selected}</p>
              {:catch err}
                <p>{err}</p>
              {/await}              
            </div>

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


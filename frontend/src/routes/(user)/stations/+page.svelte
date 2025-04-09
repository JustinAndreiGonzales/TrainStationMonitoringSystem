<script lang="ts">
  import DropdownStations from '$lib/DropdownStations.svelte';
  import Popup from '$lib/Popup.svelte';
  import GoToButton from '$src/lib/GoToButton.svelte';
  import Loading from '$lib/Loading.svelte';
  import RadioButton from '$lib/RadioButton.svelte';
  import Chart2 from '$lib/Chart2.svelte';
  import Chartt from '$lib/Chartt.svelte';
  import ETABar from '$lib/ETABar.svelte';
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';


  const trainMap = "https://iqbsmjbstzitakmfcmdo.supabase.co/storage/v1/object/public/stationimages//trainstations.jpg";

  let id = '';
  let loading = true;
  let etaSelected = 0;
  let currentSelected = 0;
  let dailySelected = 0;
  let hourlySelected = 0;

  let stationsList = [];
  let prevL = '';
  let etaL = '';
  let etaLprog = '';
  let prevR = '';
  let etaR = '';
  let etaRprog = '';

  onMount(() => {
    const url = new URL(window.location.href);
    const queryParams = new URLSearchParams(url.search);
    id = queryParams.get('id') || '';
    loading = false;
    
    if (id) {
      const sockL = new WebSocket(`wss://trenph.up.railway.app/ws/eta/${id}/left/`);
      const sockR = new WebSocket(`wss://trenph.up.railway.app/ws/eta/${id}/right/`);

      /*
      sockL.onopen = () => {
        console.log("Receiving ETA left details...");
      };
      */

      sockL.onmessage = (event) => {
        // console.log('L: ', event.data);
        etaL = event.data.slice(1, -1);

        if (!isNaN(Number(etaL))) {
          etaLprog = String(Number((20 - Number(etaL)) / 20 * 100)) + "%";
          
          if (Number(etaL) == 0) {
            etaL = "Train has arrived!"
          }
          else if (Number(etaL) > 1) {
            etaL = etaL + " mins left"
          }
          else {
            etaL = etaL + " min left"
          }
        }
      };

      /*
      sockR.onopen = () => {
        console.log("Receiving ETA right details...");
      };
      */

      sockR.onmessage = (event) => {
        // console.log('R: ', event.data);
        etaR = event.data.slice(1, -1);

        if (!isNaN(Number(etaR))) {
          etaRprog = String(Number((20 - Number(etaR)) / 20 * 100)) + "%";

          if (Number(etaR) == 0) {
            etaR = "Train has arrived!"
          }
          else if (Number(etaR) > 1) {
            etaR = etaR + " mins left"
          }
          else {
            etaR = etaR + " min left"
          }
        }
      };

      return () => {
        sockL.close();
        sockR.close();
      };
    }
  });

  async function fetchStations() {  
    const res = await fetch('https://trenph.up.railway.app/api/station/?format=json');
    if (!res.ok) throw new Error("Failed to fetch stations");
    return await res.json();
  }

  const getStationInfo = async (id: string) => {
    if (stationsList.length == 0) {
      stationsList = await fetchStations();
    }
    const res = await fetch(`https://trenph.up.railway.app/api/station/${id}/?format=json`)
    // ERROR!
    const data = await res.json();

    getPrevStations(id, data.trainLine);
    return data;
  }

  function getPrevStations(id: string, line: string) {
    let initialL = stationsList.find(x => x.id == Number(id)+1 && x.trainLine == line);
  
    if (initialL === undefined) {
      prevL = 'Train dock';
    }
    else {
      prevL = initialL.stationName;
    }

    let initialR = stationsList.find(x => x.id == Number(id)-1 && x.trainLine == line);

    if (initialR === undefined) {
      prevR = 'Train dock';
    }
    else{
      prevR = initialR.stationName;
    }
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
      {#await fetchStations()}
      <div class="flex justify-center items-center min-h-screen">
        <Loading />
      </div>
      {/await}
    {:then station}
      {#if station.isOperating}
        <div class="sm:mb-20 origin-top">
          <!-- DIV0 - HEADER -->
          <div class="relative w-full h-64">
            {#if station.stationImage}
              <img
                src={station.stationImage}
                alt="station"
                class="w-full h-full object-cover"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent opacity-80 rounded-lg"></div>
            {:else}
              <p>hello</p>
              <div class=" w-full h-full object-cover bg-gray-200"></div>
            {/if}

            <div data-testid="station-header" class="absolute bottom-4 left-8 {station.stationImage ? "text-white" : "text-black"} text-xl font-semibold">
              <div class="flex flex-col">
                <p class="inter-h1 text-[28px]">{station.stationName}</p>
                <p class="inter-body text-xl">{station.trainLine}</p>
              </div>
            </div>
  
            <div data-testid="report" class="absolute bottom-4 right-8 text-white inter-body text-[12px]">
              <button class="flex flex-col justify-end items-center bg-red-500 px-2 py-1.5 rounded-lg hover:bg-red-700" on:click={() => goto(`/stations/report?id=${station.id}`)}>
                <svg class="w-7 h-7 fill-white mb-0.5" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M512 32a480 480 0 1 0 480 480A480 480 0 0 0 512 32z m0 194.24a64 64 0 0 1 64 64c0 81.28 1.92 26.24-11.52 276.48a53.44 53.44 0 0 1-106.88 0c-13.44-248.32-11.52-192-11.52-276.48a64 64 0 0 1 65.92-64z m0 571.52a70.08 70.08 0 1 1 70.4-70.4 70.08 70.08 0 0 1-70.4 70.4z"/></svg>
                Report
                <!--
                <GoToButton text="Report" href={`/stations/report?id=${station.id}`} />
                -->
              </button>
            </div>
          </div>

          <div class="flex flex-col scale-75 sm:scale-100 mt-5 origin-top justify-center items-center space-y-5">
            <!-- DIV1 - ETA -->
            <div data-testid="eta" class="flex flex-col items-center justify-center bg-gray-200 rounded-lg w-110 p-5 space-y-2">
              <p class="inter-h1 text-lg">Next Train ETA</p>
              <div class="flex w-full scale-85">
                <RadioButton options={["Left", "Right"]} values={[0, 1]} bind:selected={etaSelected} />
              </div>

              {#if etaSelected}
                {#if !etaR}
                  <Loading />
                {:else}
                  {#if etaRprog}
                    <ETABar progress={etaRprog} size={"max-w-85"} prev={prevR} curr={station.stationName}/>
                  {/if}
                  <p class="inter-h1 text-xl">{etaR}</p>
                {/if}
              {:else}
                {#if !etaL}
                  <Loading />
                {:else}
                  {#if etaLprog}
                    <ETABar progress={etaLprog} size={"max-w-85"} prev={prevL} curr={station.stationName}/>
                  {/if}
                  <p class="inter-h1 text-xl">{etaL}</p>
                {/if}
              {/if}
            </div>

            <!-- DIV2 - CURRENT DENSITY -->
            <div data-testid="current-density" class="flex flex-col items-center justify-center bg-gray-200 rounded-lg w-110 p-5 space-y-2">
              <p class="inter-h1 text-lg">Current Density</p>
              <div class="flex w-full scale-85">
                <RadioButton options={["Left", "Right"]} values={[0, 1]} bind:selected={currentSelected} />
              </div>

              {#if currentSelected}
                {#if station.rightCCTV}
                  <p class="inter-h1 text-2xl">{station.rightCurrentDensity}</p>
                  <GoToButton text="View CCTV" href={`/stations/cctv?id=${station.id}&stream=${currentSelected+1}`}/>
                {:else}
                  <p class="inter-body text-sm">No available data for this selection.</p>
                {/if}  
              {:else}
                {#if station.leftCCTV}
                  <p class="inter-h1 text-2xl">{station.leftCurrentDensity}</p>
                  <GoToButton text="View CCTV" href={`/stations/cctv?id=${station.id}&stream=${currentSelected+1}`}/>
                {:else}
                  <p class="inter-body text-sm">No available data for this selection.</p>
                {/if}
              {/if}
            </div>

            <!-- DIV3 - DAILY DENSITY -->
            <div data-testid="daily-density" class="flex flex-col items-center justify-center bg-gray-200 rounded-lg w-110 p-5 space-y-2">
              <p class="inter-h1 text-lg">Daily Density</p>

              {#await getDailyDensity(id)}
                <Loading />
              {:then daily}
                <div class="flex w-full scale-85">
                  <RadioButton options={["Left", "Right"]} values={[0, 1]} bind:selected={dailySelected} />
                </div>
                {#if dailySelected}
                  {#if daily[dailySelected].length > 0}
                    <Chartt vals={daily[dailySelected].map(obj => obj.rightDensity)}/>
                  {:else}
                    <p class="inter-body text-sm">No available data for this selection.</p>
                  {/if}
                {:else}
                  {#if daily[dailySelected].length > 0}
                    <Chartt vals={daily[dailySelected].map(obj => obj.leftDensity)}/>
                  {:else}
                    <p class="inter-body text-sm">No available data for this selection.</p>
                  {/if}
                {/if}
              {:catch err}
                <p class="inter-body text-sm">No available data for Daily Density.</p>
              {/await}              
            </div>
            
            <!-- DIV4 - HOURLY DENSITY -->
            <div data-testid="hourly-density" class="flex flex-col items-center justify-center bg-gray-200 rounded-lg w-110 p-5 space-y-2">
              <p class="inter-h1 text-lg">Hourly Density</p>

              {#await getHourlyDensity(id)}
                <Loading />
              {:then hourly}
                <div class="flex w-full scale-85">
                  <RadioButton options={["Left", "Right"]} values={[0, 1]} bind:selected={hourlySelected} />
                </div>
                {#if hourlySelected}
                  {#if hourly[hourlySelected].length > 0}
                    <Chart2 vals={hourly[hourlySelected].map(obj => obj.rightDensity)}/>
                  {:else}
                    <p class="inter-body text-sm">No available data for this selection.</p>
                  {/if}
                {:else}
                  {#if hourly[hourlySelected].length > 0}
                    <Chart2 vals={hourly[hourlySelected].map(obj => obj.leftDensity)}/>
                  {:else}
                    <p class="inter-body text-sm">No available data for this selection.</p>
                  {/if}
                {/if}
              {:catch err}
                <p class="inter-body text-sm">No available data for Hourly Density.</p>
              {/await}              
            </div>

          </div>  
        </div>

      {:else}
        <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6">
          <h1 class="flex justify-center inter-h1 text-3xl">Stations</h1>
        
          <br>
          <div class="flex justify-center items-center">
            <img src={trainMap} alt="Train Map" class="max-w-full w-[385px] object-cover h-90 rounded-lg">
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
            <img src={trainMap} alt="Train Map" class="max-w-full w-[385px] object-cover h-90 rounded-lg">
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


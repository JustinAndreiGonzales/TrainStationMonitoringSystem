<script lang="ts">
  import DropdownStations2 from '$lib/DropdownStations2.svelte';
  import Popup from '$lib/Popup.svelte';
  import Loading from '$lib/Loading.svelte';
  import trainMap from '$lib/images/train_map.png';
  import { onMount } from 'svelte';

  let start = '';
  let end = '';
  let iStart = 1;
  let stations = [];
  let loading = true;

  onMount(() => {
      const url = new URL(window.location.href);
      const queryParams = new URLSearchParams(url.search);
      start = queryParams.get('start') || '';
      end = queryParams.get('end') || '';
      loading = false;
  });

  async function fetchStations() {
    const res = await fetch('https://trenph.up.railway.app/api/station/?format=json');
    if (!res.ok) throw new Error("Error! No database connection");
    const data = await res.json();

    stations = data;
    return data;
  }

  function findStation(id) {
    console.log(id);
    return [...stations].find(stat => stat.id === id) || null;
  }

  function setIStart(path) {
    if (path[0][2] === 0) {
      iStart = -1;
    }
  }

  const getRouteInfo = async (start: string, end: string) => {
    if (!stations.length) {
      stations = await fetchStations();
    }
    
    const res = await fetch(`https://trenph.up.railway.app/api/route/${start}/${end}/?format=json`)
    if (!res.ok) throw new Error("Error! No database connection");
    const data = await res.json();

    setIStart(data.path);

    return data;
  }

  const getLine = station => {
    if (1 <= station && station <= 20) {
        return "MRT1";
    } else if (21 <= station && station <= 33) {
        return "LRT2";
    } else {
        return "LRT3";
    }
}

const getEndStation = (start, end) => {
    let line = getLine(start);
    if (start - end < 0) {
        switch (line) {
            case "MRT1":
                return 1;
            case "LRT2":
                return 21;
            case "LRT3":
                return 34;
        }
    } else if (start - end > 0) {
        switch (line) {
            case "MRT1":
                return 20;
            case "LRT2":
                return 33;
            case "LRT3":
                return 46;
        }
    }
    return 0;
}

const stops = (num) => {
  if (num > 1) {
    return `${num} stops`;
  }
  return "1 stop";
}

</script>

<title>Routes | Train Station Monitoring System</title>

{#if true}
{#if start && end}
  {#await getRouteInfo(start, end)}
    <!-- FIX MAYBE: show page -->
    <div class="flex justify-center items-center min-h-screen">
      <Loading />
    </div>
  {:then route}
    <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-5 flex flex-col justify-center items-center">
      <h1 class="text-center inter-h1 text-3xl">Routes - {findStation(Number(start)).stationName} to {findStation(Number(end)).stationName}</h1>
      <div class="flex flex-col justify-center items-center mr-4">
        <div class="flex flex-col space-y-1">
          {#each route.path as subpath, i}
            {#if i != 0}
            <div class="grid grid-cols-[auto_1fr] gap-5 items-center">
              <span class="inter-h1 text-3xl text-center w-10">{i*3 + iStart - 1}</span>
              <p class="inter-body text-lg">Transfer train line to {findStation(subpath[0]).trainLine} at {findStation(subpath[0]).stationName} station.</p>
            </div>
            {/if}

            {#if subpath[0] != subpath[1]}
              <div class="grid grid-cols-[auto_1fr] gap-5 items-center">
                <span class="inter-h1 text-3xl text-center w-10">{i*3 + iStart}</span>
                <p class="inter-body text-lg">At {findStation(subpath[0]).trainLine} {findStation(subpath[0]).stationName} station, board the train going to {findStation(getEndStation(subpath[1],subpath[0])).stationName}.</p>
              </div>
              
              <div class="grid grid-cols-[auto_1fr] gap-5 items-center">
                <span class="inter-h1 text-3xl text-center w-10">{i*3 + iStart + 1}</span>
                <p class="inter-body text-lg">Ride for {stops(subpath[2])} and alight at {findStation(subpath[1]).stationName} station.</p>
              </div>
            {/if}
          {/each}
        </div>
        <p class="inter-h1 text-md mt-5">Total cost:</p>  
        <p class="inter-h2 text-2xl mt-[-5px]">Php {route.cost.reduce((s, a) => s + a, 0)}</p>  
      </div>
    </div>
  {:catch err}
    <!-- FIX: show page -->
    <h1 class="flex justify-center inter-h1 text-3xl">Routes</h1>
    <Popup message={"Error! No database connection"} href={"/"} text={"✕"} />
  {/await}
    
{:else}
  {#await fetchStations()}
    <!-- FIX MAYBE: show page -->
    <div class="flex justify-center items-center min-h-screen">
      <Loading />
    </div>
  {:then stations}
    <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6">
      <h1 class="flex justify-center inter-h1 text-3xl">Routes</h1>

      <br>
      <div class="flex justify-center items-center">
          <img src={trainMap} alt="Train Map" class="max-w-full w-[385px] h-auto rounded-lg">
      </div>

      <br>
      <!-- FIX: adjust to UAT specs? -->
      <DropdownStations2 allStations={stations}/>
    </div>
  {:catch error}
    <!-- FIX: show page -->
    <Popup message={"Error! No database connection"} href={"/"} text={"✕"} />
  {/await}
{/if}
{/if}



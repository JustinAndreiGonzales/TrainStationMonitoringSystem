<script lang="ts">
    import DropdownStations from '$lib/DropdownStations.svelte';
    import Popup from '$lib/Popup.svelte';
    import trainMap from '$lib/images/train_map.png';
    import { onMount } from 'svelte';

    let id = '';

    async function fetchStations() {
        const res = await fetch('https://trenph.vercel.app/api/station/?format=json');
        if (!res.ok) throw new Error("Failed to fetch stations");
        return await res.json();
    }

    onMount(() => {
        const url = new URL(window.location.href);
        const queryParams = new URLSearchParams(url.search);
        id = queryParams.get('id') || '';
    });

    const getStationInfo = async (id: string) => {
      const res = await fetch(`https://trenph.vercel.app/api/station/${id}/?format=json`)
      const data = await res.json();
      console.log(id)
      return data;
    }

  </script>

<br>
{#if id}
  {#await getStationInfo(id)}
    <br>
  {:then station}
      {#if station.isOperating}
        <p class="flex justify-center inter-h1 text-3xl">Station: {station.stationName}</p>
        <p class="flex justify-center inter-body text-3xl">ETA = {station.leftETA} vs {station.rightETA}</p>
        <p class="flex justify-center inter-body text-3xl">Density = {station.leftCurrentDensity} vs {station.rightCurrentDensity}</p>
      {:else}
        <p class="flex justify-center inter-h1 text-3xl">Station: {station.stationName}</p>
        <p class="flex justify-center inter-body text-3xl">is not currently operating :(</p>
      {/if}
  {/await}
  
{:else}
  {#await fetchStations() then stations}
    <h1 class="flex justify-center inter-h1 text-3xl">Stations</h1>

    <br>

    <div class="flex justify-center items-center">
        <img src={trainMap} alt="Train Map" class="max-w-full w-[385px] h-auto rounded-lg">
    </div>

    <br>

    <DropdownStations allStations={stations}/>

  {:catch error}
    <h1 class="flex justify-center inter-h1 text-3xl">Stations</h1>

    <br>

    <div class="flex justify-center items-center">
        <img src={trainMap} alt="Train Map" class="max-w-full w-[385px] h-auto rounded-lg">
    </div>

    <Popup message={error} />

  {/await}
{/if}


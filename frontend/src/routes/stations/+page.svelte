<script lang="ts">
    import DropdownStations from '$lib/DropdownStations.svelte';
    import trainMap from '$lib/images/train_map.png';
    import { onMount } from 'svelte';

    let id = '';

    onMount(() => {
        const url = new URL(window.location.href);
        const queryParams = new URLSearchParams(url.search);
        id = queryParams.get('id') || '';
    });

    const getStationInfo = async (id: string) => {
      // CHANGE URL!!
      const res = await fetch("https://jsonplaceholder.typicode.com/photos")
      const data = await res.json();
      const foundStation = data.find((data) => data.id === parseInt(id));
      return foundStation;
    }

  </script>

<br>
{#if id}
  {#await getStationInfo(id)}
    <br>
  {:then station}
    <!-- REPLACE: {#if station.isOperating}-->
    {#if false}
      <p class="flex justify-center inter-h1 text-3xl">Station: {station.title}</p>
      <p class="flex justify-center inter-body text-3xl">ETA = {station.leftETA} vs {station.rightETA}</p>
      <p class="flex justify-center inter-body text-3xl">Density = {station.leftCurrentDensity} vs {station.rightCurrentDensity}</p>
    {:else}
      <p class="flex justify-center inter-h1 text-3xl">Station: {station.title}</p>
      <p class="flex justify-center inter-body text-3xl">is not currently operating :(</p>
    {/if}
  {/await}
{:else}
  <h1 class="flex justify-center inter-h1 text-3xl">Stations</h1>

  <br>

  <div class="flex justify-center items-center">
      <img src={trainMap} alt="Train Map" class="max-w-full w-[385px] h-auto rounded-lg">
  </div>

  <br>

  <DropdownStations />
{/if}


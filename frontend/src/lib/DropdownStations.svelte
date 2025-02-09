<script>
  import { onMount } from "svelte";
  import StationButton from "./GoToButton.svelte";

  let trainLines = [];
  let stations = [];
  let selectedTrainLine = "";
  let selectedStation = "";
  let selectedHref = "";
  let allStations = [];

  const fetchStations = async () => {
    try {
      const response = await fetch("https://trenph.vercel.app/api/station/?format=json");
      if (!response.ok) {
        throw new Error("Failed to fetch stations.");
      }
      allStations = await response.json();

      trainLines = [...new Set(allStations.map((station) => station.trainLine))];
    } catch (error) {
      console.error("Error fetching stations:", error);
    }
  };

  onMount(() => {
    fetchStations();
  });

  $: stations = selectedTrainLine
    ? allStations.filter((station) => station.trainLine === selectedTrainLine)
    : [];

  $: if (selectedTrainLine || selectedTrainLine == "") {
    selectedStation = "";
    selectedHref = "";
  }

  $: if (selectedStation) {
    selectedHref = selectedStation;
  }
</script>

<form class="max-w-sm mx-auto">
  <label for="stations" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white inter-h2">
    Select station
  </label>

  <div class="flex items-center space-x-2">
    <div class="w-25">
      <select
        id="train-lines"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        bind:value={selectedTrainLine}
      >
        <option value="" selected>Line</option>
        {#each trainLines as line}
          <option value={line}>{line}</option>
        {/each}
      </select>
    </div>

    <div class="w-75">
      <select
        id="stations"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        bind:value={selectedStation}
        disabled={!selectedTrainLine}
      >
        <option value="" selected>Station</option>
        {#each stations as { id, stationName }}
          <option value="/stations?id={id}">{stationName}</option>
        {/each}
      </select>
    </div>

    {#if selectedHref}
      <StationButton href={selectedHref} />
    {/if}
  </div>
</form>

<style>
  .w-25 {
    width: 25%;
  }
  .w-75 {
    width: 75%;
  }
</style>

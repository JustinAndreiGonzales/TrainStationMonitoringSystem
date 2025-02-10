<script>
  import GoToButton from "./GoToButton.svelte";

  export let allStations = [];

  let trainLines = [];
  let stations = [];
  let selectedTrainLine = "";
  let selectedStation = "";
  let selectedHref = "";
  
  $: trainLines = [...new Set(allStations.map((station) => station.trainLine))];

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
        class="inter-body bg-gray-50 border border-gray-300 text-gray-900 text-[13px] rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
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
        class="inter-body bg-gray-50 border border-gray-300 text-gray-900 text-[13px] rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
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
      <GoToButton href={selectedHref} text={"→"} />
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

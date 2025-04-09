<script>
  import GoToButton from "./GoToButton.svelte";

  export let allStations = [];

  let trainLines = [];
  let stations1 = [];
  let stations2 = []; 
  let selectedTrainLine1 = "";
  let selectedTrainLine2 = "";
  let selectedStation1 = "";
  let selectedStation2 = "";

  $: trainLines = [...new Set(allStations.map((station) => station.trainLine))];

  $: stations1 = selectedTrainLine1
    ? allStations.filter((station) => station.trainLine === selectedTrainLine1)
    : [];
  
  $: stations2 = selectedTrainLine2
    ? allStations.filter((station) => station.trainLine === selectedTrainLine2)
    : [];

  $: if (selectedTrainLine1 || !selectedTrainLine1) selectedStation1 = "";
  $: if (selectedTrainLine2 || !selectedTrainLine2) selectedStation2 = "";
</script>

<div class="flex justify-center align-center">
<div class="flex items-end justify-center space-x-3 max-w-sm w-full max-h-sm">
  <div class="flex flex-col flex-grow space-y-2">
    <form class="w-full flex flex-col space-y-2">
      <label for="stations1" class="block mb-2 text-sm font-medium text-gray-900 inter-h2">
        Start station
      </label>

      <div class="flex space-x-2">
        <div class="dropdown-line">
          <select
            id="train-lines1"
            class="dropdown-select inter-body"
            bind:value={selectedTrainLine1}
          >
            <option value="" selected>Line</option>
            {#each trainLines as line}
              <option value={line}>{line}</option>
            {/each}
          </select>
        </div>

        <div class="dropdown-station">
          <select
            id="stations1"
            class="dropdown-select inter-body"
            bind:value={selectedStation1}
            disabled={!selectedTrainLine1}
          >
            <option value="" selected>Station</option>
            {#each stations1.slice().sort((a, b) => a.id - b.id) as { id, stationName }}
              <option value="{id}">{stationName}</option>
            {/each}
          </select>
        </div>
      </div>
    </form>

    <form class="w-full flex flex-col space-y-2">
      <label for="stations2" class="block mb-2 text-sm font-medium text-gray-900 inter-h2">
        End station
      </label>

      <div class="flex space-x-2">
        <div class="dropdown-line">
          <select
            id="train-lines2"
            class="dropdown-select inter-body"
            bind:value={selectedTrainLine2}
          >
            <option value="" selected>Line</option>
            {#each trainLines as line}
              <option value={line}>{line}</option>
            {/each}
          </select>
        </div>

        <div class="dropdown-station">
          <select
            id="stations2"
            class="dropdown-select inter-body"
            bind:value={selectedStation2}
            disabled={!selectedTrainLine2}
          >
            <option value="" selected>Station</option>
            {#each stations2.slice().sort((a, b) => a.id - b.id) as { id, stationName }}
              <option value="{id}">{stationName}</option>
            {/each}
          </select>
        </div>
      </div>
    </form>
  </div>


  {#if selectedStation1 && selectedStation2 && selectedStation1 !== selectedStation2}
  <div class="h-29">
    <GoToButton href={`/routes/?start=${selectedStation1}&end=${selectedStation2}`} text={"→"} />
  </div>
  {/if}
</div>
</div>

<style>
  .dropdown-line {
    width: 25%;
  }
  
  .dropdown-station {
    width: 75%;
  }
  
  .dropdown-select {
    background-color: #f9fafb;
    border: 1px solid #d1d5db;
    color: #111827;
    font-size: 13px;
    border-radius: 8px;
    padding: 10px;
    width: 100%;
  }
</style>
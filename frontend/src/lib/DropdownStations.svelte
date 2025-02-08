<script lang="ts">
    import StationButton from './GoToButton.svelte';
   
    const getStations = async () => {
      // CHANGE URL!!
      const res = await fetch("https://jsonplaceholder.typicode.com/photos")
      const data = await res.json();
      return data;
    }

    let selectedHref = "";
  </script>
  
  {#await getStations()}
    <br>
  {:then station}
    <form class="max-w-sm mx-auto"> 
      <label for="stations" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white inter-h2">
        Select station
      </label>
          
      <div class="flex items-center space-x-2">
        <select
          id="stations"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          bind:value={selectedHref}
        >  
          <option value="" selected>Choose a station</option>

          {#each station as { id, url, title }}
            <!-- REPLACE IF URL FIXED: <option value="/stations?id={id}">{stationName} ({trainLine})</option> -->
            <option value="stations?id={id}">{url} ({title})</option>
          {/each}

        </select>

        {#if selectedHref}
          <StationButton href={selectedHref} />
        {/if}
      </div>
    </form>
  {/await}
<script>
  import Checkbox2 from "$lib/Checkbox2.svelte"
  import { onMount } from "svelte";
    import Loading from "./Loading.svelte";

  export let edit = false;
  export let ogTitle = "";
  export let subject = "";
  export let ogBody = ""; 
  export let body = ""; 
  export let tags = [];
  export let selectedTags = [];
  export let func;
  export let disabled = false;
  let options = [];

  // [SP4] FIX! 
  // horizontal overflow 

  async function fetchTagChoices() {
      const res = await fetch(`https://trenph.up.railway.app/api/station/?format=json`);
      if (!res.ok) throw new Error("Failed to fetch stations");

      const data = await res.json();
      data.sort((a, b) => a.id - b.id);

      const stations = ['LRT1', 'LRT2', 'MRT3'];
      let fetchedOptions = [];

      stations.forEach(line => {
        let c = data
          .filter(d => d.trainLine === line)
          .map(station => ({
            id: String(station.id),
            label: station.stationName,
            checked: selectedTags.includes(station.stationName)
          }));
        
        fetchedOptions.push({
          id: line,
          label: line,
          checked: selectedTags.includes(line),
          children: c
        });
      });

      options = [...fetchedOptions];
    }

  onMount(() => {
    fetchTagChoices();
  }); 

  function equalArr(a, b) {
    if (a.length !== b.length) return false;

    const sortedA = [...a].sort();
    const sortedB = [...b].sort();

    return sortedA.every((v, i) => v === sortedB[i]);
  }

  function submitOk(a, b, c, d) {
    let notEmpty = (a && b);

    if(edit) {
      let wasChanged = (ogTitle != a || ogBody != b || !(equalArr(c, d)) && options.length);
      return wasChanged && notEmpty;
    }

    return notEmpty;
  }

  function postBoxOverflow() {
    if (edit) return "mb-[-7px]";
    return "mb-[-6px]";
  }
</script>

<div class="flex flex-col items-center justify-center space-y-4 w-full">
  <div class="border border-gray-300 rounded-lg w-full max-w-200 bg-white">
    <input
      type="text"
      placeholder="Subject"
      class="w-full px-4 py-2 text-gray-900 focus:outline-gray-500 focus:rounded-t-lg text-sm inter-body border-b border-gray-300"
      bind:value={subject}
      disabled={disabled}
    />
    <textarea
      placeholder="Body"
      class="w-full h-auto px-4 py-2 {postBoxOverflow()} text-gray-900 focus:outline-gray-500 text-sm inter-body resize-none border-b border-gray-300"
      rows={5}
      bind:value={body}
      disabled={disabled}
    ></textarea>
    <div class="flex flex-row space-x-3 items-center">
      <Checkbox2 bind:selected={tags} disabled={disabled} bind:options={options}/> 
      {#if !options.length}
        <div class="ml-[-5px] scale-75">
          <Loading />
        </div>
      {:else if !tags.length}
        <p class="text-gray-400 text-[12px] inter-body">Select tags</p>
      {:else}
        <div class="flex flex-row space-x-3 w-full overflow-x-auto whitespace-nowrap">
        {#each tags as t}
          <p class="bg-gray-400 text-white my-1.5 px-3 py-1 rounded-sm text-[12px] inter-body">{t}</p>
        {/each} 
        </div>
      {/if}
    </div>
  </div>
    

  {#if submitOk(subject, body, tags, selectedTags)}
    <button
      class="mx-auto bg-blue-600 max-w-200 hover:bg-blue-700 text-white inter-body text-sm w-full py-2 px-4 rounded"
      on:click={func}
    >
      Submit
    </button>
  {:else}
    <button
      class="mx-auto bg-gray-300 max-w-200 text-white inter-body text-sm w-full py-2 px-4 rounded"
      disabled={true}
    >
      Submit
    </button>
  {/if}
</div>
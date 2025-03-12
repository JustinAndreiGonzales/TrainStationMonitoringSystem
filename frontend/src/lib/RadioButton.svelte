<script>
  export let options;
  export let values;
  export let selected;
</script>

<div class="inline-flex border-2 border-blue-600 rounded-lg overflow-hidden">
  {#each values as val, i}
    <label
      class="px-4 py-2 cursor-pointer transition-all duration-200 text-blue-600 border-blue-600"
      class:bg-blue-600={selected === val}
      class:text-white={selected === val}
    >
      <input type="radio" bind:group={selected} value={val} class="hidden" />
      {options[i]}
    </label>
  {/each}
</div>

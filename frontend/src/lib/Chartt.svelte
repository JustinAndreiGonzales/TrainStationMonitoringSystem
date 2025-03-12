<script>
  export let vals = []; 
  let days = ['M', 'T', 'W', 'Th', 'F', 'S', 'S'];

  function toInt(num) {
    return Math.floor(num);
  }
</script>

<div class="flex flex-row space-x-2 mt-3 mx-5">
  {#each vals as val, i}
  <div class="flex flex-col justify-center items-center space-y-2">
    <div class="w-10 bg-gray-50 h-[100px] relative overflow-hidden border-gray-400 rounded">
      <!-- <p class="inter-body text-[10px]">{val}</p> -->  
      <div
        class="bg-blue-600 absolute bottom-0 w-full transition-all duration-300"
        style="height: {toInt(val)}px"
      ></div>
    </div>

    <p class="inter-body text-sm text-gray-500">{days[i]}</p>
  </div>
  {/each}
</div>

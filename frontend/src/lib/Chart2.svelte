<script>
  export let vals = []; 
  let days = ['06:00', '09:00', '12:00', '03:00', '05:00', '09:00'];

  function toInt(num) {
    return Math.floor(num);
  }
</script>

<div class="flex flex-row space-x-2 mt-3 mx-5">
  {#each vals as val, i}
  <div class="flex flex-col justify-center items-center">
    <div class="w-[10px] bg-gray-50 h-[100px] relative overflow-hidden border-gray-400 rounded ">
      <!--<p class="inter-body text-[10px]">{val}</p>-->
      <div
        class="bg-blue-600 absolute bottom-0 w-full transition-all duration-300"
        style="height: {toInt(val)}px"
      ></div>
    </div>
  </div>
  {/each}

  
</div>

<div class="flex flex-row justify-center items-center space-x-[31px]">
  {#each days as d}  
    <p class="inter-body text-[10px] text-gray-500">{d}</p>
  {/each}
</div>
<script>
  export let text = "";
  export let href = "";
  export let bgColor = "bg-blue-600";
  export let hvrColor = "hover:bg-blue-700";
  export let txtColor = "text-white";
  export let isBold = "font-bold"
  
  function navigate() {
    window.location.href = href;
  }
</script>

<button
  class="max-w-sm mx-auto {bgColor} {hvrColor} {txtColor} {isBold} py-2 px-4 rounded"
  on:click={navigate}
  disabled={!href}
>
  {text}  
</button>

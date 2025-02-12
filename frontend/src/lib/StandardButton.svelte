<script>
    export let src = ""; 
    export let text = "Button"; 
    export let href = "";  
</script>
  
<div class="h-auto">
<a
  href={href}
  class="flex flex-row items-center bg-blue-600 hover:bg-blue-700 text-white py-3 px-4 rounded-lg inter-body space-x-1"
>
  {#if src}
    <img src={src} alt={text} class="w-6 mr-2" />
  {/if}
  <p>  </p>
  <span class="text-[15px]">{@html text}</span>
</a>
</div>
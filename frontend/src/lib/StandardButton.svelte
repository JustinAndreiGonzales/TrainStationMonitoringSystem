<script>
    export let src = ""; 
    export let text = "Button"; 
    export let href = "";  
    export let bg = "bg-blue-600";
    export let bgHover = "hover:bg-blue-700";
</script>
  
<div class="h-auto">
<a
  href={href}
  class="flex flex-row items-center {bg} {bgHover} text-white py-3 px-4 rounded-lg inter-body space-x-1"
>
  {#if src}
    <img src={src} alt={text} class="w-6 mr-2" />
  {/if}
  <p>  </p>
  <span class="text-[15px]">{@html text}</span>
</a>
</div>
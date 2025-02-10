<script>
    export let src = ""; 
    export let text = "Button"; 
    export let href = "";  
</script>
  
<a
  href={href}
  class="flex items-center bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-lg inter-body"
>
  {#if src}
    <img src={src} alt={text} class="w-4 h-4 mr-2" />
  {/if}
  <span class="text-sm">{text}</span>
</a>
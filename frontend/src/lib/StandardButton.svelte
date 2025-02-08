<script>
    export let src = ""; 
    export let text = "Button"; 
    export let href = "";  
  </script>
  
  {#if href}
    <a
      href={href}
      class="flex items-center bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-lg"
    >
      {#if src}
        <img src={src} alt={text} class="w-6 h-6 mr-2" />
      {/if}
      <span>{text}</span>
    </a>
  {:else}
    <button class="flex items-center bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-lg">
      {#if src}
        <img src={src} alt={text} class="w-6 h-6 mr-2" />
      {/if}
      <span>{text}</span>
    </button>
  {/if}
  
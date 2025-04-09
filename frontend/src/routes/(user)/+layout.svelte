<script>
  import '$src/app.css'
  import NavBar from '$lib/NavBar.svelte';
  import { page } from '$app/stores';

  $: currentUrl = $page.url;
  function isSubpath() {
    let afterHTTP = String(currentUrl).split('//')[1];
    let subpath = afterHTTP.substring(afterHTTP.indexOf('/')+1); 
    let basepath = '';

    if(subpath.includes('/')){
      basepath = subpath.split('/')[0];
      subpath = subpath.split('/')[1];
    }

    if(subpath.includes('?')){
      if(basepath) {
        subpath = subpath.split('?')[1];
      }
      else {
        subpath = subpath.split('?')[0];
        // basepath = subpath.split('?')[0];
      }
    }

    return basepath + (basepath ? '?' : '') + subpath;
    // return (basepath.length > 0);
  };

  function handleClick() {
    console.log(isSubpath());
    window.location.href = '/' + isSubpath();
    // window.history.back();
  }
</script>

{#if String(currentUrl).includes('?')}
  <button
    aria-label="back"
    class="fixed top-4 left-4 z-50 cursor-pointer bg-white/70 p-2 rounded-full hover:bg-white transition"
    on:click={handleClick}
  >
    <svg class="w-5 h-6.5 rotate-90 text-black" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
    </svg>
  </button>
{/if}
<slot />
<NavBar />
  
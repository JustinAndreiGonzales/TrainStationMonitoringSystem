<script>
  import { page } from "$app/stores";
  import { goto } from '$app/navigation';

  async function logout() {
        await fetch('/admin', { method: 'DELETE' }); 
        goto('/admin', { replaceState: true });
    }

  // FIX: EDIT ICONS
  let links = [
    { name: "Home", href: "/admin/home", img: "/a.png" },
    { name: "Create account", href: "/admin/create-account", img: "/e.png" },
    { name: "Announcements", href: "/admin/announcements", img: "/b.png" },
    { name: "Reports", href: "/admin/reports", img: "/f.png" },
    { name: "Log out", href: "/admin", img: "/g.png" },  ];

  function currentLink() {
    return [...links].find(link => $page.url.pathname.startsWith(link.href)); 
  }

  function forceLink(href, event) {
    let matchingLink = currentLink();

    if (matchingLink && matchingLink.href === href) {
      event.preventDefault(); 
      window.location.href = href;
    }
  }
  
  function textHighlight(href) {
    let link = currentLink();
    
    if (link && link.href == href) {
      return "text-sm font-semibold inter-h1";   
    }
    return "text-xs inter-body";
  }
</script>

<!-- DISABLE create account -->
<footer class="fixed bottom-0 w-full bg-blue-700 shadow-inner ">
  <ul class="flex justify-around list-none m-0 p-0 mt-1">
    {#each links as link}
      <li class="flex flex-col items-center py-2">
        {#if link.name == "Log out" }
          <a href="{link.href}" 
          class="flex flex-col items-center text-white space-y-1"
          on:click={logout}
          >
            <img src={link.img} alt={"icon.png"} class="w-5"/>
            <span class={textHighlight(link.href)}>{link.name}</span>
          </a>
        {:else}
          <a href="{link.href}" 
          class="flex flex-col items-center text-white space-y-1"
          on:click={event => forceLink(link.href, event)}
          >
            <img src={link.img} alt={"icon.png"} class="w-5"/>
            <span class={textHighlight(link.href)}>{link.name}</span>
          </a>
        {/if}
      </li>
    {/each}
  </ul>
</footer>

<style>
</style>
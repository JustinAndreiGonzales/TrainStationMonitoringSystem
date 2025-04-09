<script>
  import '$src/app.css'
  import NavBar from '$lib/NavBar2.svelte';  
  import { browser } from '$app/environment';

  let role = '';

  if (browser) {
    role = localStorage.getItem("role") || "";
  }
  
</script>

<slot />
<NavBar superAdmin={"superAdmin" === role}/>
  
<script>
  import '$src/app.css';
  import { browser } from '$app/environment';

  let username = '';

  if (browser) {
    username = localStorage.getItem("username") || "";
  }
</script>

<title>Home | Train Station Monitoring System</title>
<main class="flex justify-center items-center h-screen pb-10">
  {#if username}
    <p class="inter-h1 text-[50px]">Welcome {username}!</p>
  {/if}
</main>

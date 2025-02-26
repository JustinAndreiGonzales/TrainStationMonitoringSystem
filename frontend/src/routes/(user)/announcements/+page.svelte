<script lang="ts">
  import AnnouncementsList from '$lib/AnnouncementsList.svelte';
  import Loading from '$lib/Loading.svelte';
  import Popup from '$lib/Popup.svelte';

  let ctr = 3;

  async function fetchAnnouncements() {
      const res = await fetch(`https://trenph.up.railway.app/api/announcements/?format=json`);
      if (!res.ok) throw new Error("Failed to fetch announcements");
      return await res.json();
  }
</script>

<title>Announcements | Train Station Monitoring System</title>

<div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
  <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Announcements</h1>
  {#await fetchAnnouncements()}
    <Loading />
  {:then announcements}
    <AnnouncementsList max={announcements.count} posts={announcements.results} />
  {:catch error}
    <!-- FIX: popup centering -->
    <Popup message={error} href={"/admin/home"} text={"✕"} />
  {/await}
</div>
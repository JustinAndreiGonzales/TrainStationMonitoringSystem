<script lang="ts">
  import AnnouncementsList from '$lib/AnnouncementsList.svelte';
  import Loading from '$lib/Loading.svelte';
  import Popup from '$lib/Popup.svelte';

  let ctr = 3;

  async function fetchAnnouncements() {
      const res = await fetch(`https://trenph.up.railway.app/api/announcements/`);
      if (!res.ok) throw new Error("Failed to fetch announcements");
      return await res.json();
  }
</script>

<title>Announcements | Train Station Monitoring System</title>

{#await fetchAnnouncements()}
  <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
    <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Announcements</h1>
    <Loading />
  </div>
{:then announcements}
  <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
    <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Announcements</h1>
    <AnnouncementsList max={announcements.count} posts={announcements.results} />
  </div>
{:catch error}
    <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
      <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Announcements</h1>
    </div>
    <Popup message={error} href={"/"} text={"✕"} />
{/await}
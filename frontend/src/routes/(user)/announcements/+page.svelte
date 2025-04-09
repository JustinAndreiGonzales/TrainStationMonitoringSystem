<script lang="ts">
  import AnnouncementsList from '$lib/AnnouncementsList.svelte';
  import Loading from '$lib/Loading.svelte';
  import Popup from '$lib/Popup.svelte';
  import Checkbox from '$lib/Checkbox3.svelte';

  let ctr = 3;
  let filtered = [];

  async function fetchAnnouncements() {
      const res = await fetch(`https://trenph.up.railway.app/api/announcements/`);
      if (!res.ok) throw new Error("Failed to fetch announcements");
      return await res.json();
  }
</script>

<title>Announcements | Train Station Monitoring System</title>

{#await fetchAnnouncements()}
  <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
    <div class="flex flex-col items-center justify-center inter-h1 text-3xl origin-top mt-6 space-y-3">
      <h1>Announcements</h1>
      <Checkbox disabled={true} />
    </div>
    <Loading />
  </div>
{:then announcements}
  <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
    <div class="flex flex-col items-center justify-center inter-h1 text-3xl origin-top mt-6 space-y-3">
      <h1>Announcements</h1>
      <Checkbox bind:selected={filtered}/>
    </div>
    <AnnouncementsList max={announcements.count} posts={announcements.results} filters={filtered} />
  </div>
{:catch error}
    <div class="scale-80 sm:scale-100 md:scale-100 origin-top mt-6 space-y-7">
      <h1 class="flex justify-center inter-h1 text-3xl origin-top mt-6">Announcements</h1>
    </div>
    <Popup message={error} href={"/"} text={"✕"} />
{/await}
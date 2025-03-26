<script lang="ts">
  import { onMount } from 'svelte';

  import Checkbox from '$lib/Checkbox.svelte';
  import List from '$lib/dummy/FooList.svelte';
  import Checkbox2 from '$lib/Checkbox2.svelte'
  import EtaBar from '$lib/ETABar.svelte';

  let eta = '';
  let time = '';

  let options = [
  {
    id: 'checkbox-item-1',
    label: 'LRT-1',
    checked: false,
    children: [
      { id: 'sub-item-1', label: 'LRT-1A', checked: false },
      { id: 'sub-item-2', label: 'LRT-1B', checked: false }
    ]
  },
  {
    id: 'checkbox-item-2',
    label: 'LRT-2',
    checked: false
  },
  {
    id: 'checkbox-item-3',
    label: 'MRT-3',
    checked: false,
    children: [
      { id: 'sub-item-3', label: 'MRT-3A', checked: false }
    ]
  }
];


  onMount(() => {
    const socket = new WebSocket("wss://trenph.up.railway.app/ws/eta/3/left/");

    socket.onopen = () => {
      console.log("Receiving ETA details...");
    };

    socket.onmessage = (event) => {
      const now = new Date();
      const timeStr = now.toISOString();

      eta = event.data.slice(1, -1);

      if (!isNaN(Number(eta))) {
        if (Number(eta) == 0) {
          eta = "Train is stopping..."
        }
        else if (Number(eta) > 1) {
          eta = eta + " mins left"
        }
        else {
          eta = eta + " min left"
        }
      }
      
      console.log("Received:", eta, " @ ", timeStr);
    };

    return () => {
      socket.close();
    };
  });  

  async function fetchAnnouncements() {
      const res = await fetch(`https://trenph.up.railway.app/api/announcements/`);
      if (!res.ok) throw new Error("Failed to fetch announcements");
      return await res.json();
  }

  let stuff = [];
</script>

<title>Announcements | Train Station Monitoring System</title>

<p>{eta}</p>
<br>
<div class="flex flex-row space-x-5">
  <p>TAGS: </p>
  {#each stuff as s}
    <p>{s}</p>
  {/each}
</div>
<Checkbox bind:selected={stuff} />
<Checkbox2 />
<br> 
<br> 
<List />
<br>

<EtaBar size={"max-w-md"} progress={"100%"}/>


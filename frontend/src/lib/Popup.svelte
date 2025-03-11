<script>
    import GoToButton from "./GoToButton.svelte";
    export let message = "";
    export let href = "";
    export let text = "";
    export let color = "bg-red-700"
    export let txtColor = "text-red-700"
  </script>
  
  <div class="fixed inset-0 backdrop-blur-[2px] z-40"></div>

  <div
    class={`fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-4/5 sm:w-auto ${color} text-white text-lg rounded-lg shadow-lg p-8 z-50`}
    role="alert"
  >
    <div class="flex flex-row items-center justify-center justify-between m-auto space-x-6">
      <span class="flex text-left inter-body font-xs">{message}</span>
      <span>
        <GoToButton href={href} text={text} bgColor={"bg-neutral-50"} hvrColor={"hover:bg-neutral-200"} txtColor={txtColor} isBold={""}/>
      </span>
    </div>
  </div>
  
  <style>
  </style>
  
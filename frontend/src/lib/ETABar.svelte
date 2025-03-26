<script>
  export let size = "";
  export let prev = "Station1";
  export let curr = "Station2";
  export let progress = "45%";
</script>

<div class="mt-6.5 relative w-full {size}">
  <div class="w-full bg-white rounded-full h-2.5 relative">
    <div class="bg-blue-600 h-2.5 rounded-full relative" style="width: {progress}">
      <div class="absolute left-0 top-1/2 -translate-y-1/2 w-4 h-4 bg-blue-600 rounded-full"></div>
      <div class="absolute right-0 top-1/2 -translate-y-1/2 w-4 h-4 bg-blue-600 rounded-full"></div>
    </div>
  </div>

  <div class="absolute left-0 -top-6 text-gray-700 text-sm font-medium inter-h1">{prev}</div>
  <div class="absolute right-0 -top-6 text-gray-700 text-sm font-medium inter-h1">{curr}</div>
</div>

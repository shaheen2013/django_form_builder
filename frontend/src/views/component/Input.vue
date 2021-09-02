<template>
    <div >
        <input :type="inputType" class="form-control" />
    </div>
</template>

<script>
    export default {
        name: "Input",
        props:['name','inputType']
    };
</script>
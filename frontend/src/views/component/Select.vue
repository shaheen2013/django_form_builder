<template>
    <div>
        <select class="form-control">
            <option value=""> select</option>
            <option v-for="(item, index) in options" value="" :key="index"> {{item}} </option>
        </select>
    </div>
</template>

<script>
    export default {
        name: "Select",
        props:['name', 'select_options'],
        data(){
            return{
                options:this.select_options.split(',')
            }
        }
    };
</script>
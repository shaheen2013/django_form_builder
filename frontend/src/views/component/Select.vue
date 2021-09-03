<template>
    <div>
        <select class="form-control" :name="name" v-model="propReplace">
            <option value=""> select</option>
            <option v-for="(item, index) in options" :value="item" :key="index"> {{item}}</option>
        </select>
    </div>
</template>

<script>
    export default {
        name    : "Select",
        props   : ['name', 'select_options'],
        data() {
            return {
                options: this.select_options.split(',')
            }
        },
        computed: {
            propReplace: {
                get() {
                    return this.value;
                },
                set(newValue) {
                    this.$emit('input', newValue);
                }
            }
        }
    };
</script>
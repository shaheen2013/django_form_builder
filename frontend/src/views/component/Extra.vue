<template>
    <div>
        <div class="text-start">
            <label class="form-label ">Options seperate by <span class="text-danger">(,) </span></label>
            <input v-model="propReplace" type="text" class="form-control" placeholder="options seperate by (,)"/>
        </div>
    </div>
</template>

<script>
    export default {
        name    : "Textarea",
        props   : ['name', 'value'],
        mounted() {
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
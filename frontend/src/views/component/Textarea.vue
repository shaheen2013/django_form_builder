<template>
    <div>
        {{ name}}
        <textarea :name="name" v-model="propReplace" class="form-control"></textarea>
    </div>
</template>

<script>
    export default {
        name    : "Textarea",
        props   : ['name', 'value'],
        data() {
            return {
                abc: ''
            }
        },
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
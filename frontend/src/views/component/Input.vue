<template>
    <div>
        <div v-if="inputType==='radio'" class="text-start">
            <div class="row pt-2" v-for="(item,index) in radioInputs">
                <div class="col-1">
                    <i class="far fa-dot-circle"></i>
                </div>
                <div class="col-10">
                    <input  type="text" class="form-control">
                </div>
                <div class="col-1">
                    <button class="btn btn-danger" type="button" @click="removeRadioInput(index)">-</button>
                </div>
            </div>
            <div class="float-end pt-2">
                <button class="btn btn-success" type="button" @click="addRadioInput">+</button>
            </div>
        </div>
        <div v-else-if="inputType==='checkbox'" class="text-start">
            <div class="row pt-2" v-for="(item,index) in radioInputs">
                <div class="col-1">
                    <i class="fas fa-square-full"></i>
                </div>
                <div class="col-10">
                    <input @keyup="checkboxInput($event,item.id)" v-model="item.name" type="text" class="form-control">
                </div>
                <div class="col-1">
                    <button class="btn btn-danger" type="button" @click="removeRadioInput(index)">-</button>
                </div>
            </div>
            <div class="float-end pt-2">
                <button class="btn btn-success" type="button" @click="addRadioInput">+</button>
            </div>
        </div>
        <div v-else>
            <input v-model="propReplace" :type="inputType" class="form-control"/>
        </div>

    </div>
</template>

<script>
    export default {
        name    : "Input",
        props   : ['name', 'select_options', 'inputType'],
        data() {
            return {
                id         : 1,
                radioInputs: [{
                    id   : 0,
                    name : '',
                    value: '',
                }],
            }
        },
        methods : {
            addRadioInput() {
                let id = this.id++;
                this.radioInputs.push(
                    {
                        id   : id,
                        name : '',
                        value: '',
                    }
                )

            },
            removeRadioInput(id) {
                this.radioInputs.splice(id, 1)
            },
            checkboxInput(e, id) {
                console.log('aa', e.target.value, id);
                this.$emit('customChange', this.radioInputs);
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
            },

        },

    };
</script>
<template>
    <div class="container">
        <h1>Feadback survey</h1>
        <div class="row">
            <div class="col-md-4">
                <ul class="list-group">
                    <draggable
                            class="dragArea list-group"
                            :list="formFieldTypes"
                            :group="{ name: 'people', pull: 'clone', put: false }"
                            :clone="cloneDog"
                            @change="log"
                    >
                        <transition-group>
                            <div v-for="element in formFieldTypes" :key="element.id">
                                <li class="list-group-item">{{element.title}}</li>
                            </div>
                        </transition-group>
                    </draggable>
                </ul>
            </div>
            <div class="col-md-8">
                <draggable
                        class="dragArea list-group border p-5"
                        :list="formFields"
                        group="people"
                        @change="log"
                >
                    <div class="list-group-item border-top mb-3" v-for="(element,index) in formFields" :key="index">

                        <div class="col-md-12">
                            <div class="row border-bottom ">
                                <div class="col-md-1">
                                    <i class="fas fa-align-justify"></i>
                                </div>
                                <div class="col-md-9 pb-2">
                                    <input type="text" class="form-control" placeholder="Question title">
                                </div>
                                <div class="col-md-2">
                                    <span @click="removeField(index)"><i class="fas fa-times"></i></span>
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="row mt-2">
                                    <div class="col-md-9 ">
                                        <component :is="`${element.type}_input`" :name="element.name"
                                                   :select_options="element.value" :inputType="element.input_type"></component>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </draggable>
            </div>
        </div>

    </div>
</template>

<script>
    import draggable from 'vuedraggable'
    import Select    from './component/Select'
    import Textarea  from './component/Textarea'
    import Input     from './component/Input'

    let idGlobal = 8;
    export default {
        name      : 'Home',
        components: {
            Input,
            draggable,
            'textarea_input': Textarea,
            'select_input'  : Select,
            'text_input'    : Input
        },
        data() {
            return {
                formFieldTypes: [],
                formFields    : [],
            }
        },
        mounted() {
            this.getFormFieldTypes()
        },
        methods   : {
            getFormFieldTypes() {
                ApiService.get('/formbuilder/form_fields/')
                    .then(res => this.formFieldTypes = res.data)
                    .catch(
                        // error => NotificationService.error("Please login")
                    )
            },
            log: function (evt) {
                window.console.log(evt);
            },
            cloneDog({id, type, title, value}) {
                let input_type = type;
                if (!['text', 'select', 'textarea'].includes(type)) {
                    type = 'text'
                }
                return {
                    id        : id,
                    title     : title,
                    type      : type,
                    value     : value,
                    input_type: input_type,
                };
            },
            removeField(id) {
                console.log(id);
                this.formFields.splice(id, 1)
            }
        }
    }
</script>

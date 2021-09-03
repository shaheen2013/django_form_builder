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
            <div class="col-md-8 border pt-3">
                <div class="col-md-9 pb-2 text-start">
                    <label class="form-label ">Form Title</label>
                    <input v-model="formTitle" type="text" class="form-control"
                           placeholder="Form title">
                </div>
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
                                    <i class="fas fa-arrows-alt"></i>
                                </div>
                                <div class="col-md-9 pb-2">
                                    <input v-model="element.title" type="text" class="form-control"
                                           placeholder="Question title">
                                </div>
                                <div class="col-md-2">
                                    <span @click="removeField(index)"><i class="fas fa-times"></i></span>
                                </div>
                            </div>
                            <div class="form-group">
                                <div class="row mt-2">
                                    <div class="col-md-9 ">
                                        <component v-if="element.input_type" :is="`${element.input_type}_input`"
                                                   :name="element.input_value"
                                                   :select_options="element.value"
                                                   v-model="element.input_value"></component>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </draggable>
                <div class="col-md-8 text-start mt-3">
                    <button class="btn btn-info " :class="formFields.length == 0 ? 'disabled' : ''" type="button"
                            @click="submitForm">Submit
                    </button>
                    <button class="btn btn-info "  type="button"
                            @click="preview">Preview
                    </button>
                </div>
            </div>
        </div>
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Launch demo modal
        </button>

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="list-group-item border-top mb-3" v-for="(element,index) in formFields" :key="index">

                            <div class="col-md-12">
                                <div class="row border-bottom ">
                                    <div class="col-md-1">
                                        <i class="fas fa-arrows-alt"></i>
                                    </div>
                                    <div class="col-md-9 pb-2">
                                        <input v-model="element.title" type="text" class="form-control"
                                               placeholder="Question title">
                                    </div>
                                    <div class="col-md-2">
                                        <span @click="removeField(index)"><i class="fas fa-times"></i></span>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <div class="row mt-2">
                                        <div class="col-md-9 ">
                                            <component v-if="element.input_type" :is="`${element.input_type}_input`"
                                                       :name="element.input_value"
                                                       :select_options="element.value"
                                                       v-model="element.input_value"></component>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary">Save changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import draggable from 'vuedraggable'
    import Extra     from './component/Extra'
    import About     from './About'

    let idGlobal = 8;
    export default {
        name      : 'Home',
        components: {
            draggable,
            'extra_input': Extra,
        },
        data() {
            return {
                formFieldTypes: [],
                formFields    : [],
                formTitle     : ''
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
                //window.console.log(evt);
            },
            cloneDog({id, type, title, value}) {
                let input_type = '';
                if (['radio', 'checkbox'].includes(type)) {
                    input_type = 'extra'
                }
                return {
                    id         : id,
                    title      : '',
                    type       : type,
                    value      : value,
                    input_type : input_type,
                    input_value: '',
                };
            },
            removeField(id) {
                console.log(id);
                this.formFields.splice(id, 1)
            },
            submitForm() {
                this.formFields.push(this.formTitle);
                ApiService.post('/formbuilder/', {data: this.formFields})
                    .then(res => {
                        this.formFields.pop();
                        console.log(res);
                        NotificationService.error("Please login")
                    })
                    .catch(
                        // error => NotificationService.error("Please login")
                    )
            },
            preview(){

            }
        }
    }
</script>

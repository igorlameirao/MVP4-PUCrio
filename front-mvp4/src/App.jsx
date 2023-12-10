//hooks
import { useEffect, useState } from "react";

//Estilizacao
import {
  Box,
  Flex,
  FormControl,
  FormLabel,
  Input,
  Button,
  Grid,
} from "@chakra-ui/react";

//services
import { Service } from "./services/Service";

const App = () => {
  const [acidezFixa, setAcidezFixa] = useState();
  const [acidezVolatil, setAcidezVolatil] = useState();
  const [acidoCitrico, setAcidoCitrico] = useState();
  const [acucarResidual, setAcucarResidual] = useState();
  const [cloretos, setCloretos] = useState();

  const [dioxidoEnxofreLivre, setDioxidoEnxofreLivre] = useState();
  const [dioxidoEnxofreTotal, setDioxidoEnxofreTotal] = useState();
  const [densidade, setDensidade] = useState();
  const [ph, setPh] = useState();
  const [sulfatos, setSulfatos] = useState();
  const [alcool, setAlcool] = useState();

  const handleSubmit = (e) => {
    const service = new Service();

    const data = {
        acidezFixa,
        acidezVolatil,
        acidoCitrico,
        acucarResidual,
        cloretos,
        dioxidoEnxofreLivre,
        dioxidoEnxofreTotal,
        densidade,
        ph,
        sulfatos,
        alcool
    }

    service.Submit(data).then(response => {
      console.log(data)
      alert(response.data)
    }).catch(err => {
      alert("Erro")
    });
  };

  return (
    <Flex
      h="100vh"
      align="center"
      justify="center"
      fontSize="20px"
      fontFamily="poppins"
    >
      <Box w="80%" h="100vh" py={10} px={2}>
          <Grid templateColumns="repeat(2, 1fr)" gap={6}>
            <FormControl>
              <FormLabel>Ácidez Fixa</FormLabel>
              <Input type="number"
                name="acidezFixa"
                value={acidezFixa}
                onChange={(e) => { setAcidezFixa(e.target.value) }}
              />
            </FormControl>
            <FormControl>
              <FormLabel>Ácidez Volatil</FormLabel>
              <Input type="number"
                name="acidezVolatil"
                value={acidezVolatil}
                onChange={(e) => { setAcidezVolatil(e.target.value) }} />
            </FormControl>
            <FormControl>
              <FormLabel>Ácido Citrico</FormLabel>
              <Input type="number"
                name="acidoCitrico"
                value={acidoCitrico}
                onChange={(e) => { setAcidoCitrico(e.target.value) }} />
            </FormControl>
            <FormControl>
              <FormLabel>Açúcar Residual</FormLabel>
              <Input type="number"
                name="acucarResidual"
                value={acucarResidual}
                onChange={(e) => { setAcucarResidual(e.target.value) }} />
            </FormControl>
            <FormControl>
              <FormLabel>Cloretos</FormLabel>
              <Input type="number"
                name="cloretos"
                value={cloretos}
                onChange={(e) => { setCloretos(e.target.value) }} />
            </FormControl>
            <FormControl>
              <FormLabel>Dioxido Enxofre Livre</FormLabel>
              <Input type="number"
                name="dioxidoEnxofreLivre"
                value={dioxidoEnxofreLivre}
                onChange={(e) => { setDioxidoEnxofreLivre(e.target.value) }} />
            </FormControl>
            <FormControl>
              <FormLabel>dioxido Enxofre Total</FormLabel>
              <Input type="number"
                name="dioxidoEnxofreTotal"
                value={dioxidoEnxofreTotal}
                onChange={(e) => { setDioxidoEnxofreTotal(e.target.value) }} />
            </FormControl>
            <FormControl>
              <FormLabel>Densidade</FormLabel>
              <Input type="number"
                name="densidade"
                value={densidade}
                onChange={(e) => { setDensidade(e.target.value) }} />
            </FormControl>
            <FormControl>
              <FormLabel>PH</FormLabel>
              <Input type="number"
                name="ph"
                value={ph}
                onChange={(e) => { setPh(e.target.value) }} />
            </FormControl>
            <FormControl>
              <FormLabel>Sulfatos</FormLabel>
              <Input type="number"
                name="sulfatos"
                value={sulfatos}
                onChange={(e) => { setSulfatos(e.target.value) }} />
            </FormControl>
            <FormControl>
              <FormLabel>alcool</FormLabel>
              <Input type="number"
                name="alcool"
                value={alcool}
                onChange={(e) => { setAlcool(e.target.value) }} />
            </FormControl>
          </Grid>

          <Flex justify="flex-end" mt={4}>
            <Button colorScheme="blue" type="submit" onClick={handleSubmit}>
              Enviar
            </Button>
          </Flex>
      </Box>
    </Flex >
  )
};

export default App;

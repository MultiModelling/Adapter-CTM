<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:esdl="http://www.tno.nl/esdl" version="7" id="51f76bad-d3ea-499e-b362-70b4d14154de" description="Standard file Meso Case" esdlVersion="v2207" name="MapEditorMesoCase">
  <instance xsi:type="esdl:Instance" id="b3a80d08-e9b7-4a5e-ac54-69c9327c151b" name="Yara Site">
    <area xsi:type="esdl:Area" name="Untitled area" id="46cdcfee-e304-4b55-aa20-5d024bf2af17">
      <asset xsi:type="esdl:Electrolyzer" id="21570d9f-8d1f-4df4-bf3d-d4ac7eea47d3" efficiency="0.7" technicalLifetime="25.0" state="ENABLED" name="electrolyzer">
        <KPIs xsi:type="esdl:KPIs">
          <kpi xsi:type="esdl:StringKPI" name="yara_production_h2_electrolysis" value="1."/>
        </KPIs>
        <port xsi:type="esdl:InPort" id="cfb83f0a-b8d2-4af1-acb0-0e58455ca843" connectedTo="2a0328b6-5e7b-4aa3-95ba-d64afa86e05a" name="In_Electricity" carrier="e8346314-97f4-455c-804c-488d68de223b"/>
        <port xsi:type="esdl:OutPort" id="203f3a36-f9b0-4f8e-99fb-80917d485bdb" name="H2_out" carrier="d6d532f3-92d0-4bcd-9f40-dc629a9bd1be" connectedTo="ffccae3a-fdd1-48c1-9023-d3f073a6f725"/>
        <port xsi:type="esdl:InPort" id="7a0816bb-ff7a-4002-82f5-b71cf1eab4ac" connectedTo="ccf5d762-abf5-4c6d-8665-b2c4173b56bc" name="Water_In" carrier="8a313264-6d2c-41b8-a04e-e1a4cacccf5b"/>
        <port xsi:type="esdl:OutPort" id="66a1fbd7-49b5-403b-98aa-aa75ab263b96" name="Out_Electricity" carrier="e8346314-97f4-455c-804c-488d68de223b" connectedTo="c14bb774-48cc-4fcd-81d5-a96d47a1c894"/>
        <port xsi:type="esdl:OutPort" id="59fdda72-3cca-43e3-9ef9-9fc2e22bde0e" name="O2_OutPort" carrier="f76c3a6c-d4ca-4e5e-b351-d849075f4087" connectedTo="07918488-eb3f-49b1-a090-7072d48b1593"/>
        <geometry xsi:type="esdl:Point" lon="3.8512229919433594" lat="51.27920606558368"/>
        <behaviour xsi:type="esdl:InputOutputRelation" mainPort="203f3a36-f9b0-4f8e-99fb-80917d485bdb">
          <mainPortRelation xsi:type="esdl:PortRelation" ratio="9.01" port="7a0816bb-ff7a-4002-82f5-b71cf1eab4ac">
            <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" unit="GRAM" multiplier="MEGA" id="2b1d3d40-aa8f-44b5-9892-a597b70e61f9"/>
          </mainPortRelation>
          <mainPortRelation xsi:type="esdl:PortRelation" ratio="203.0" port="cfb83f0a-b8d2-4af1-acb0-0e58455ca843">
            <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" unit="JOULE" multiplier="GIGA" id="0c02dad0-d833-4bd2-a42a-36edddbefc05"/>
          </mainPortRelation>
        </behaviour>
        <costInformation xsi:type="esdl:CostInformation">
          <investmentCosts xsi:type="esdl:SingleValue" value="100.0"/>
          <marginalCosts xsi:type="esdl:SingleValue" value="1211.0"/>
        </costInformation>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" id="814880dd-b0c4-4f0c-9654-1ddc1c70049f" name="ElectricityDummyDemand">
        <port xsi:type="esdl:InPort" id="c14bb774-48cc-4fcd-81d5-a96d47a1c894" connectedTo="66a1fbd7-49b5-403b-98aa-aa75ab263b96" name="In" carrier="e8346314-97f4-455c-804c-488d68de223b"/>
        <geometry xsi:type="esdl:Point" lon="3.8584756851196294" lat="51.276387290096615"/>
      </asset>
      <asset xsi:type="esdl:GasConversion" id="74c94568-be15-4110-bc07-4afc56fee0c1" state="DISABLED" name="yara_SMR" type="SMR">
        <KPIs xsi:type="esdl:KPIs">
          <kpi xsi:type="esdl:StringKPI" name="yara_production_h2_smr" value="0."/>
        </KPIs>
        <port xsi:type="esdl:InPort" id="91db20dd-8c56-444b-98bb-194f097d4ea5" connectedTo="6b3f9a8d-1515-4486-bbce-6b985ca0efb5" name="Port" carrier="344d205a-1c31-4c4c-85a8-c3aa181a7057"/>
        <port xsi:type="esdl:OutPort" id="1a788cf1-7cd6-43a9-8414-041e583aee7a" name="Out_N2" carrier="e6485461-1606-4cd4-833c-8967f4941d19" connectedTo="0afe53d4-8bf6-4ce0-90da-e589f2b5d1ff"/>
        <port xsi:type="esdl:OutPort" id="dafb4a5d-7f50-4401-8f7b-419db1276660" name="Out_CO2" carrier="ff6a5c83-a673-478b-92ff-66937a592dac" connectedTo="c49fa3f2-2705-40d2-8d62-539d28e5c571"/>
        <port xsi:type="esdl:OutPort" id="321fa0db-9d48-43a6-ab53-7a53df2c86ce" name="Out_H2" carrier="d6d532f3-92d0-4bcd-9f40-dc629a9bd1be" connectedTo="ffccae3a-fdd1-48c1-9023-d3f073a6f725"/>
        <port xsi:type="esdl:InPort" id="a68ff1c2-9454-40aa-9982-ffe1e165a9b3" connectedTo="ff1e9fdf-6f55-4e07-8a0f-291bc6256c04" name="In_N2" carrier="e6485461-1606-4cd4-833c-8967f4941d19"/>
        <port xsi:type="esdl:InPort" id="b5c5ce43-3f6d-4cc3-b27c-51f42385f67e" connectedTo="78425d36-6f37-4cda-8b00-e370d4d69ec2" name="In_O2" carrier="f76c3a6c-d4ca-4e5e-b351-d849075f4087"/>
        <port xsi:type="esdl:InPort" id="847cbb1f-bdf4-4d53-a8df-57efa417a019" connectedTo="ccf5d762-abf5-4c6d-8665-b2c4173b56bc" name="In_H2O" carrier="8a313264-6d2c-41b8-a04e-e1a4cacccf5b"/>
        <geometry xsi:type="esdl:Point" lon="3.8482618331909184" lat="51.277649049078"/>
        <behaviour xsi:type="esdl:InputOutputRelation" mainPort="321fa0db-9d48-43a6-ab53-7a53df2c86ce">
          <mainPortRelation xsi:type="esdl:PortRelation" ratio="3.58" port="91db20dd-8c56-444b-98bb-194f097d4ea5">
            <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" unit="GRAM" multiplier="MEGA" id="653b01fb-8f62-4127-be1e-40c2a2bebdea"/>
          </mainPortRelation>
          <mainPortRelation xsi:type="esdl:PortRelation" ratio="3.72" port="847cbb1f-bdf4-4d53-a8df-57efa417a019">
            <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" unit="GRAM" multiplier="MEGA" id="627212d7-3ddd-4f11-b0f7-c809e4209bbb"/>
          </mainPortRelation>
          <mainPortRelation xsi:type="esdl:PortRelation" ratio="4.67" port="a68ff1c2-9454-40aa-9982-ffe1e165a9b3">
            <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" unit="GRAM" multiplier="MEGA" id="915df1da-38a8-4c0d-8e78-64e9836a1e4e"/>
          </mainPortRelation>
          <mainPortRelation xsi:type="esdl:PortRelation" ratio="4.67" port="1a788cf1-7cd6-43a9-8414-041e583aee7a">
            <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" unit="GRAM" multiplier="MEGA" id="7fb014d7-b5d5-4cd1-987c-243e817dfec3"/>
          </mainPortRelation>
          <mainPortRelation xsi:type="esdl:PortRelation" ratio="6.46" port="dafb4a5d-7f50-4401-8f7b-419db1276660">
            <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" unit="GRAM" multiplier="MEGA" id="40d900f2-7c41-466c-8beb-7b647c52e0c7"/>
          </mainPortRelation>
          <mainPortRelation xsi:type="esdl:PortRelation" ratio="1.39" port="b5c5ce43-3f6d-4cc3-b27c-51f42385f67e">
            <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" unit="GRAM" multiplier="MEGA" id="b475ab2b-da07-4a2b-a9f3-7d2577d54c3f"/>
          </mainPortRelation>
        </behaviour>
      </asset>
      <asset xsi:type="esdl:GenericConsumer" id="7d721bb9-f949-4891-b444-e6e2357563af" name="GenericConsumer_H2">
        <port xsi:type="esdl:InPort" id="ffccae3a-fdd1-48c1-9023-d3f073a6f725" connectedTo="203f3a36-f9b0-4f8e-99fb-80917d485bdb 321fa0db-9d48-43a6-ab53-7a53df2c86ce" name="In_SMR" carrier="d6d532f3-92d0-4bcd-9f40-dc629a9bd1be"/>
        <geometry xsi:type="esdl:Point" lon="3.856158256530762" lat="51.2749509903577"/>
      </asset>
      <asset xsi:type="esdl:SinkConsumer" id="a113f602-eaef-4dfa-b7f3-4568b4cecf47" name="Consumer_N2">
        <port xsi:type="esdl:InPort" id="0afe53d4-8bf6-4ce0-90da-e589f2b5d1ff" connectedTo="1a788cf1-7cd6-43a9-8414-041e583aee7a" name="In" carrier="e6485461-1606-4cd4-833c-8967f4941d19"/>
        <geometry xsi:type="esdl:Point" lon="3.848776817321778" lat="51.27324616510048"/>
      </asset>
      <asset xsi:type="esdl:ElectricityProducer" id="ebe77404-e686-418f-830a-d48f96cae650" name="ElectricityProducer">
        <port xsi:type="esdl:OutPort" id="2a0328b6-5e7b-4aa3-95ba-d64afa86e05a" name="Out" carrier="e8346314-97f4-455c-804c-488d68de223b" connectedTo="cfb83f0a-b8d2-4af1-acb0-0e58455ca843"/>
        <geometry xsi:type="esdl:Point" lon="3.849291801452637" lat="51.285218875238584"/>
      </asset>
      <asset xsi:type="esdl:Import" id="0ec05565-ad45-4771-9b65-b3f6d7e2e17b" name="Import_N2">
        <port xsi:type="esdl:OutPort" id="ff1e9fdf-6f55-4e07-8a0f-291bc6256c04" name="Out" carrier="e6485461-1606-4cd4-833c-8967f4941d19" connectedTo="a68ff1c2-9454-40aa-9982-ffe1e165a9b3"/>
        <geometry xsi:type="esdl:Point" lon="3.84572982788086" lat="51.28371574661717"/>
      </asset>
      <asset xsi:type="esdl:Import" id="3e563f62-a496-4b30-8cf0-f4a0102bbd10" name="Import_O2">
        <port xsi:type="esdl:OutPort" id="78425d36-6f37-4cda-8b00-e370d4d69ec2" name="Out" carrier="f76c3a6c-d4ca-4e5e-b351-d849075f4087" connectedTo="b5c5ce43-3f6d-4cc3-b27c-51f42385f67e"/>
        <geometry xsi:type="esdl:Point" lon="3.8440132141113286" lat="51.282749423668605"/>
      </asset>
      <asset xsi:type="esdl:GenericProducer" id="53696bad-beff-4959-a376-7410ef3c006c" name="GenericProducer_CH4">
        <port xsi:type="esdl:OutPort" id="6b3f9a8d-1515-4486-bbce-6b985ca0efb5" name="Out" carrier="344d205a-1c31-4c4c-85a8-c3aa181a7057" connectedTo="91db20dd-8c56-444b-98bb-194f097d4ea5"/>
        <geometry xsi:type="esdl:Point" lon="3.8418674468994145" lat="51.281514648092795"/>
      </asset>
      <asset xsi:type="esdl:SinkConsumer" id="15c6ed1b-765c-42dc-be92-86986bed29c4" name="Consumer_CO2">
        <port xsi:type="esdl:InPort" id="c49fa3f2-2705-40d2-8d62-539d28e5c571" connectedTo="dafb4a5d-7f50-4401-8f7b-419db1276660" name="In" carrier="ff6a5c83-a673-478b-92ff-66937a592dac"/>
        <geometry xsi:type="esdl:Point" lon="3.8516521453857426" CRS="WGS84" lat="51.274212687972586"/>
      </asset>
      <asset xsi:type="esdl:Import" id="733b0935-0846-430d-87bc-29dfb6d9913e" name="Import_H2O">
        <port xsi:type="esdl:OutPort" id="ccf5d762-abf5-4c6d-8665-b2c4173b56bc" name="Out" carrier="8a313264-6d2c-41b8-a04e-e1a4cacccf5b" connectedTo="7a0816bb-ff7a-4002-82f5-b71cf1eab4ac 847cbb1f-bdf4-4d53-a8df-57efa417a019"/>
        <geometry xsi:type="esdl:Point" lon="3.847103118896485" lat="51.28446731707717"/>
      </asset>
      <asset xsi:type="esdl:SinkConsumer" id="284b55f8-4585-4586-b07e-a121efe49360" name="Consumer_O2">
        <port xsi:type="esdl:InPort" id="07918488-eb3f-49b1-a090-7072d48b1593" connectedTo="59fdda72-3cca-43e3-9ef9-9fc2e22bde0e" name="In" carrier="f76c3a6c-d4ca-4e5e-b351-d849075f4087"/>
        <geometry xsi:type="esdl:Point" lon="3.859763145446778" lat="51.27861547932833"/>
      </asset>
    </area>
  </instance>
  <energySystemInformation xsi:type="esdl:EnergySystemInformation" id="9ce2523e-96dd-4112-85aa-50470bbe8e15">
    <carriers xsi:type="esdl:Carriers" id="6f5ed289-a1a4-419f-b230-19a41d76536a">
      <carrier xsi:type="esdl:GasCommodity" id="344d205a-1c31-4c4c-85a8-c3aa181a7057" name="CH4"/>
      <carrier xsi:type="esdl:EnergyCommodity" id="d6d532f3-92d0-4bcd-9f40-dc629a9bd1be" name="H2"/>
      <carrier xsi:type="esdl:EnergyCommodity" id="8a313264-6d2c-41b8-a04e-e1a4cacccf5b" name="H2O"/>
      <carrier xsi:type="esdl:EnergyCommodity" id="e6485461-1606-4cd4-833c-8967f4941d19" name="N2"/>
      <carrier xsi:type="esdl:EnergyCommodity" id="f76c3a6c-d4ca-4e5e-b351-d849075f4087" name="O2"/>
      <carrier xsi:type="esdl:EnergyCommodity" id="ff6a5c83-a673-478b-92ff-66937a592dac" name="CO2"/>
      <carrier xsi:type="esdl:EnergyCarrier" id="e8346314-97f4-455c-804c-488d68de223b" name="Electricity">
        <emissionUnit xsi:type="esdl:QuantityAndUnitType" multiplier="KILO" perUnit="JOULE" id="0aa114a6-ec9a-4328-bcf6-293796794fbb" unit="GRAM" physicalQuantity="EMISSION" perMultiplier="GIGA"/>
        <energyContentUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="ENERGY" id="8b057368-f60f-4ef4-a923-9e7942910473"/>
      </carrier>
    </carriers>
  </energySystemInformation>
</esdl:EnergySystem>

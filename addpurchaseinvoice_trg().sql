
CREATE OR REPLACE FUNCTION addpurchaseinvoice_trg()
  RETURNS trigger AS
$BODY$ DECLARE 
con integer;
BEGIN
--select * from account_invoice
select count(*) into con from account_invoice_line  where invoice_id=new.id;

IF con > 1 THEN
 Raise exception '%','Solo puede relacionar un pedido de compra a la factura de su proveedor ';
END IF;

 RETURN NEW;
END 

; $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION addpurchaseinvoice_trg()
  OWNER TO postgres;


CREATE TRIGGER  addpurchaseinvoice_trg
  BEFORE INSERT OR UPDATE 
  ON account_invoice
  FOR EACH ROW
  EXECUTE PROCEDURE  addpurchaseinvoice_trg();

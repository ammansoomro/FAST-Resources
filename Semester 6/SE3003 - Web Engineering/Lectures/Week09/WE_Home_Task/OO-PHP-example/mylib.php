<?php 
	class person {
		protected $name; 
		public $height;		
		protected $social_insurance;
		private $pin_no;
		function __construct($persons_name) {		
			$this->name = $persons_name;		
		}		
		public function set_name($new_name) {
		 	 $this->name = $new_name;
		}	
		function get_name() {		
		 	 return $this->name;		
		}		
		public function get_pin_no(){
			return $this->pin_no;  
		}
		public function set_pin_no($new_pin){
			$this->pin_no = $new_pin; 
		}    
	} 
	// 'extends' is the keyword that enables inheritance
	class employee extends person 
	{
		//Overriding methods
		public  function set_name($new_name) {
			if ($new_name ==  "Alina") {
				$this->name = strtoupper($new_name);
			}
		 	else if ($new_name ==  "Ali") {
				$this->name = strtolower($new_name);
			} else {
				person::set_name($new_name);
			} 
		}

	function __construct($employee_name)  {
		$this->set_name($employee_name);
	}
}
?>